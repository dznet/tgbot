from api.admins.models import Admins
from api.admins.models import AdminsSchema
from api.basemodels import datetime
from api.basemodels import timedelta
from api.basemodels import validate
from api.basemodels import SQLAlchemyError
from config import Development as config
from flask import Blueprint
from flask import g
from flask import jsonify
from flask import make_response
from flask import request
from flask import session
from flask_restful import Api
from flask_restful import Resource
from functools import wraps
import jwt
from jwt.exceptions import DecodeError
from jwt.exceptions import ExpiredSignatureError
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

signin = Blueprint('signin', __name__)
endpoint = Api(signin)
schema = AdminsSchema()

def create_token(account):
  payload = {
    'sub': account.id,
    'iat': datetime.utcnow(),
    'exp': datetime.utcnow() + timedelta(days=1),
    'scope': account.roles}
  token = jwt.encode(payload, config.SECRET_KEY)
  return token.decode('unicode_escape')

def parse_token(req):
  token = req.headers.get('Authorization').split()[1]
  return jwt.decode(token, config.SECRET_KEY, algorithms='HS256')

def is_superuser(roles):
  return 'superuser' in roles

def is_admin(roles):
  return 'admin' in roles

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if not request.headers.get('Authorization'):
      response = jsonify(message='Missing authorization header')
      response.status_code = 401
      return response
    try:
      payload = parse_token(request)
      g.id = payload['sub']
      g.roles = payload['scope']
    except DecodeError:
      response = jsonify(message='Token is invalid')
      response.status_code = 401
      return response
    except ExpiredSignatureError:
      response = jsonify(message='Token has expired')
      response.status_code = 401
      return response
    return f(*args, **kwargs)
  return decorated_function


class SignIn(Resource):

  def post(self):
    raw_dict = request.get_json(force=True)
    data = raw_dict['data']['attributes']
    admin = Admins.query.filter_by(username=data['username']).first()
    if admin == None:
      response = make_response(jsonify({"message": "Wrong username."}))
      response.status_code = 401
      return response
    if check_password_hash(admin.password, data['password']):
      token = create_token(admin)
      return {'token': token}
    else:
      response = make_response(jsonify({"message": "Wrong password."}))
      response.status_code = 401
      return response

endpoint.add_resource(SignIn, 'signin.json')


class Resource(Resource):
  method_decorators = [login_required]

from api.basemodels import db
from api.baseviews import Blueprint
from api.baseviews import request
from api.baseviews import make_response
from api.baseviews import jsonify
from api.baseviews import session
from api.baseviews import g
from api.baseviews import Api
from api.baseviews import SQLAlchemyError
from api.baseviews import ValidationError
from api.baseviews import Resource
from api.baseviews import is_admin
from api.baseviews import is_superuser
from api.baseviews import generate_password_hash
from api.admins.models import Admins
from api.admins.models import AdminsSchema

admins = Blueprint('admins', __name__)
schema = AdminsSchema()
endpoint = Api(admins)


class CreateListAdmins(Resource):

    def get(self):
      if is_superuser(g.roles):
        results = schema.dump(Admins.query.all(), many=True).data
        return results
      if is_admin(g.roles):
        results = schema.dump(Admins.query.filter_by(id=g.id), many=True).data
        return results

    def post(self):
      if is_superuser(g.roles):
        raw_dict = request.get_json(force=True)
        try:
          schema.validate(raw_dict)
          request_dict = raw_dict['data']['attributes']
          request_dict['roles'] = 'admin'
          admin = Admins(request_dict['roles'],
                         request_dict['username'],
                         generate_password_hash(request_dict['password']),
                         request_dict['messager_id'],
                         request_dict['is_active'],)
          admin.add(admin)
          query = Admins.query.get(admin.id)
          results = schema.dump(query).data
          return results, 201

        except ValidationError as err:
          response = jsonify({"error": err.messages})
          response.status_code = 403
          return response

        except SQLAlchemyError as e:
          db.session.rollback()
          response = jsonify({"error": str(e)})
          response.status_code = 403
          return response
        # esle: pass


class GetUpdateDeleteAdmin(Resource):

  def get(self, id):
    results = schema.dump(Admins.query.get_or_404(id)).data
    return results

  def patch(self, id):
    raw_dict = request.get_json(force=True)
    try:
      schema.validate(raw_dict)
      request_dict = raw_dict['data']['attributes']
      request_dict['password'] = generate_password_hash(request_dict['password'])
      if is_superuser(g.roles):
        admin = Admins.query.get_or_404(id)
      if is_admin(g.roles):
        admin = Admins.query.filter_by(id=g.id)
      for key, value in request_dict.items():
        setattr(admin, key, value)
      admin.update()
      return self.get(id)

    except ValidationError as err:
      response = jsonify({"error": err.messages})
      response.status_code = 401
      return response

    except SQLAlchemyError as e:
      db.session.rollback()
      response = jsonify({"error": str(e)})
      response.status_code = 401
      return response

  def delete(self, id):
      if is_superuser(g.roles):
          admin = Admins.query.get_or_404(id)
      if is_admin(g.roles):
          admin = Admins.query.filter_by(id=g.id)
      try:
          delete = admin.delete(admin)
          responseonse = make_response()
          responseonse.status_code = 204
          return responseonse

      except SQLAlchemyError as e:
          db.session.rollback()
          response = jsonify({"error": str(e)})
          response.status_code = 401
          return response


endpoint.add_resource(CreateListAdmins, '.json')
endpoint.add_resource(GetUpdateDeleteAdmin, '/<int:id>.json')

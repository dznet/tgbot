from api.basemodels import Schema
from api.basemodels import fields
from api.basemodels import validate
from api.basemodels import db
from api.basemodels import CRUD_MixIn


class Roles(db.Model, CRUD_MixIn):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(33), unique=True)

    def __init__(self,  name, ):
      self.name = name

class RolesSchema(Schema):

  error = 'Enter a value between 4 and 32 characters long.'
  not_blank = validate.Length(min=4, max=32, error=error)

  id = fields.Integer(dump_only=True)
  name = fields.String(validate=not_blank)

  def get_top_level_links(self, data, many):
    if many:
      self_link = "/roles/"
    else:
      self_link = "/roles/{}".format(data['id'])
    return {'self': self_link}

  class Meta:
    type_ = 'roles'

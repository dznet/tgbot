from api.basemodels import db
from api.basemodels import fields
from api.basemodels import validate
from api.basemodels import Account
from api.basemodels import AccountSchema


class Admins(Account):

  id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)

  def __init__(self, roles, username, password, messager_id, is_active,):
    super().__init__(roles, username, password, messager_id, is_active,)

  __tablename__ = 'admins'
  __mapper_args__ = {
    'polymorphic_identity': 'admin',
  }


class AdminsSchema(AccountSchema):

  def get_top_level_links(self, data, many):
    if many:
      self_link = "/admins/"
    else:
      self_link = "/admins/{}".format(data['id'])
    return {'self': self_link}

  class Meta:
    type_ = 'admins'

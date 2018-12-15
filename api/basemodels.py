from datetime import datetime
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow_jsonapi import fields
from marshmallow_jsonapi import Schema
from marshmallow import validate
from marshmallow import ValidationError

db = SQLAlchemy()


class CRUD_MixIn():

  def add(self, resource):
    db.session.add(resource)
    return db.session.commit()

  def update(self):
    return db.session.commit()

  def delete(self, resource):
    db.session.delete(resource)
    return db.session.commit()


class Account(db.Model, CRUD_MixIn):
  class Meta:
    abstract = True

  type = db.Column(db.String(50))
  id = db.Column(db.Integer, primary_key=True)
  roles = db.Column(db.ForeignKey('roles.name'))
  relation = db.relationship('Roles', backref='user')
  username = db.Column(db.String(32), nullable=False, unique=True)
  password = db.Column(db.String(250), nullable=False, unique=True)
  messager_id = db.Column(db.Integer, unique=True)
  first_name = db.Column(db.String(32))
  last_name = db.Column(db.String(32))
  is_active = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
  last_active = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

  __mapper_args__ = {
    'polymorphic_identity': 'account',
    'polymorphic_on': type
  }

  def __init__(self, roles, username, password, messager_id, is_active,):
    self.roles = roles
    self.username = username
    self.password = password
    self.messager_id = messager_id
    self.is_active = is_active


class AccountSchema(Schema):

  error = 'Enter a value between 4 and 32 characters long.'
  blank_user = validate.Length(min=4, max=32, error=error)

  error = 'Enter a value between 8 and 64 characters long.'
  blank_pass = validate.Length(min=8, max=64, error=error)

  id = fields.Integer(dump_only=True)
  roles = fields.String(dump_only=True)
  username = fields.String(validate=blank_user)
  password = fields.String(validate=blank_pass)
  messager_id = fields.Integer(dump_only=True)
  first_name = fields.String(dump_only=True)
  last_name = fields.String(dump_only=True)
  is_active = fields.Integer(dump_only=True)

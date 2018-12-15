from api.basemodels import db
from api.baseviews import Blueprint
from api.baseviews import request
from api.baseviews import make_response
from api.baseviews import jsonify
from api.baseviews import Api
from api.baseviews import Resource
from api.baseviews import SQLAlchemyError
from api.baseviews import ValidationError
from api.roles.models import Roles
from api.roles.models import RolesSchema

roles = Blueprint('roles', __name__)
schema = RolesSchema(strict=True)
endpoint = Api(roles)


class CreateListRoles(Resource):

    def get(self):
        roles_query = Roles.query.all()
        results = schema.dump(roles_query, many=True).data
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            role = Roles(request_dict['name'],)
            role.add(role)
            query = Roles.query.get(role.id)
            results = schema.dump(query).data
            return results, 201

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp


class GetUpdateDeleteRole(Resource):

    def get(self, id):
        role_query = Roles.query.get_or_404(id)
        result = schema.dump(role_query).data
        return result

    def patch(self, id):
        role = Roles.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            for key, value in request_dict.items():
                setattr(role, key, value)

            role.update()
            return self.get(id)

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 401
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

    def delete(self, id):
        role = Roles.query.get_or_404(id)
        try:
            delete = role.delete(role)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp


endpoint.add_resource(CreateListRoles, '.json')
endpoint.add_resource(GetUpdateDeleteRole, '/<int:id>.json')

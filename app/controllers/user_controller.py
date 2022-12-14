"""
user_controller.py
~~~~~~~~
API controller module containing users endpoints
"""
from flask import request, jsonify
from flask.wrappers import Response
from app.services.user_service import UserService
from flask_restx import Namespace, Resource

user_api = Namespace("USUARIOS", description=" CRUD usuario")

@user_api.route("/users")
class UsersDAO(Resource):
    """ Endpoint  usuarios
    Esta clase contiene los endpoints relacionados a obtener usuarios y crear nuevos usuarios
    """
    @user_api.expect(validate=True)
    def get(self) -> Response:
        """ List users
        GET : /api/v1/users
        """

        """
        if not request.json:
            return Response(status=errors['BadRequest'].get('status'), response=errors['BadRequest'].get('response'))
        """
        api_data = request.json

        try:
            users = UserService.get_many_service()
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))
        api_data['users'] = users
        return jsonify(api_data)

    def post(self) -> Response:
        """ Insert new user
        POST : /api/v1/users
        """
        return jsonify("new")

@user_api.route("/user/<string:user_id>")
#@user_api.doc(params={'uid': {'description': 'user UID'},
                # 'param1': {'description': 'blabla', 'in': 'query', 'type': 'int'}})
class UserDAO(Resource):
    """ Endpoint usuario
    Esta clase contiene los endpoints de editar un usuario y eliminar un usuario
    """
    @user_api.expect(validate=True)
    def put(self, user_id) -> Response:
        """ Edit one user
        PUT : /api/v1/users/{userId}
        """
        return jsonify(user_id)

    def delete(self, user_id) -> Response:
        """ Delete one user
        DELETE : /api/v1/users
        """
        return jsonify("delete")
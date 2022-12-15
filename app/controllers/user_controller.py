"""
user_controller.py
~~~~~~~~
API controller module containing users endpoints
"""
from flask import request, jsonify
from flask.wrappers import Response
from app.services.user_service import UserService
from flask_restx import Namespace, Resource, fields, Api, reqparse
from app.errors import errors
import logging
import random

user_api = Namespace("Usuarios", description=" CRUD usuario")

user_fields = user_api.model('Nuevo Usuario', {
    'name': fields.String(description='Nombre Completo', required=True),
    'age': fields.Integer(min=1, required=True),
})

@user_api.route("/users")

class UsersDAO(Resource):

    def get(self) -> Response:
        try:
            users = UserService.get_list()
            return jsonify(list(users))
        except Exception as e:
            logging.exception(e)
            return False

    @user_api.doc(params={'name': {'description': 'nombre usuario', 'in': 'data', 'type': 'string'},
                 'age': {'description': 'Edad', 'in': 'data', 'type': 'int'}})
    @user_api.doc(model=user_fields)
    def post(self) -> Response:
        try:
            logging.info(f" request json -> {str(request.json())}")
            result = UserService.create()
            return jsonify(list(result))
        except Exception as e:
            logging.exception(e)
            return False

@user_api.route("/user/<string:user_id>")
class UserDAO(Resource):

    @user_api.expect(validate=True)

    @user_api.doc(params={
        'name': {'description': 'Nombre del usuario', 'in': 'form'},
        'age': {'description': 'Edad del usuario', 'in': 'form', 'type': 'int'}
        })
    def put(self, user) -> Response:
        try:
            UserService.update(user)
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))
        return jsonify(user)

    def delete(self, user_id) -> Response:
        try:
            UserService.delete(user_id)
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))
        return jsonify(user_id)
"""
entity_controller.py
~~~~~~~~
API controller module containing entities endpoints
"""
from flask import request, jsonify
from flask.wrappers import Response
from app.services.entity_service import EntityService
from flask_restx import Namespace, Resource
from app.errors import errors

entity_api = Namespace("Entidades", description=" CRUD Entidades")

@entity_api.route("/entities")
class entitiesDAO(Resource):
    """ Endpoint entidades
    Esta clase contiene los endpoints relacionados a obtener entidades y crear nuevos Entidades
    """
    @entity_api.expect(validate=True)

    def get(self) -> Response:
        try:
            entities = EntityService.get_list()
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))
        return jsonify(list(entities))

    def post(self, entity) -> Response:
        """ Insert new entity
        POST : /api/v1/entities
        """
        try:
            """# EntityService.insert(entity)"""
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))
        return jsonify("new")

@entity_api.route("/entity/<string:entity_id>")

class entityDao(Resource):
    """ Endpoint institucion
    Esta clase contiene los endpoints de editar un institucion y eliminar un institucion
    """
    @entity_api.expect(validate=True)
    def put(self, entity) -> Response:
        try:
            """# EntityService.update(entity)"""
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))
        return jsonify(entity)

    def delete(self, entity) -> Response:
        try:
            """#EntityService.delete(entity)"""
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))
        return jsonify(entity)
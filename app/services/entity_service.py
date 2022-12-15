from app import mongo
from app.models.entity_model import Entity
import logging

class EntityService(object):

    @staticmethod
    def create(name, address):
        try:
            newEntity = Entity(name, address)
            result = newEntity.create()
            return result
        except Exception as e:
            logging.exception(e)
            return False

    @staticmethod
    def get_list():
        try:
            entities = Entity.getList()
            return entities
        except Exception as e:
            logging.exception(e)
            return False

    @staticmethod
    def update(entity):
        try:
            result = Entity.update(entity)
            return result
        except Exception as e:
            logging.exception(e)
            return False

    @staticmethod
    def delete(entity_id):
        try:
            result = Entity.delete(entity_id)
            return result
        except Exception as e:
            logging.exception(e)
            return False
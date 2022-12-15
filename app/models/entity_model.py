from app import mongo
import logging
import random

class Entity():
    def __init__(self, name, address):
        self.name = str(name),
        self.address = str(address),
        self.entity_id = str(random.randint(1,1000))


    @staticmethod
    def create():
        try:
            result = mongo.db.entities.insertOne(self.to_json())
            return result
        except Exception as e:
            logging.exception(e)
            return None

    @staticmethod
    def getList():
        try:
            entities = mongo.db.entities.find({},{"entity_id": 1, "name": 1, "address": 1, "_id": 0})
            return entities
        except Exception as e:
            logging.exception(e)
            return None

    @staticmethod
    def update(user):
        try:
            result = mongo.db.entities.updateOne({"entity_id": user.id},
                {"$set": {
                    "name": user.name,
                    "address": user.address,
                }}
            )
            return result
        except Exception as e:
            logging.exception(e)
            return None

    @staticmethod
    def delete(entity_id):
        try:
            result = mongo.db.entities.deleteOne({"entity_id": entity_id})
            return result
        except Exception as e:
            logging.exception(e)
            return None

    def to_json(self):
        return{
            'entity_id': self.entity_id,
            'name': self.name,
            'address': self.address
        }
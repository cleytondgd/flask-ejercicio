from app import mongo
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
import json
from flask import jsonify
import logging
import random

class User():
    def __init__(self, name, age):
        self.user_id = str(random.randint(1,1000)),
        self.age = age,
        self.name = name

    @classmethod
    def create(self):
        try:
            result_id = mongo.db.users.insert_one({ "user_id": self.user_id,  "age": self.age, "name": self.name }).inserted_id
            return str(result_id)
        except Exception as e:
            logging.exception(e)
            return None

    @staticmethod
    def getList():
        try:
            users = mongo.db.users.find({},{"user_id": 1, "name": 1, "age": 1, "_id": 0})
            return users
        except Exception as e:
            logging.exception(e)
            return None

    @classmethod
    def update(self,user_id, name, age):
        try:
            logging.info(f"SALIDAAAAAA:  {user_id}/{name}/{age}")
            finding = { "user_id": user_id }
            newValues = { "$set": { "name": name, "age": age}}

            result = mongo.db.users.update_one(finding, newValues)
            return str(result)
        except Exception as e:
            logging.exception(e)
            return None

    @staticmethod
    def delete(user_id):
        try:
            result = mongo.db.users.delete_one({"user_id": user_id})
            return f"Deleted user count: {str(result.deleted_count)}"
        except Exception as e:
            logging.exception(e)
            return None

    @classmethod
    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'age': self.age
        }
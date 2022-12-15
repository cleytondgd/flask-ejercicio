from app import mongo
import logging
import random

class User():
    def __init__(self, name, age):
        self.name = str(name),
        self.age = int(age),
        self.user_id = str(random.randint(1,1000))


    @staticmethod
    def create():
        try:
            result = mongo.db.users.insertOne(self.to_json())
            return result
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

    @staticmethod
    def update(user):
        try:
            result = mongo.db.users.updateOne({"user_id": user.id},
                {"$set": {
                    "name": user.name,
                    "age": user.age,
                }}
            )
            return result
        except Exception as e:
            logging.exception(e)
            return None

    @staticmethod
    def delete(user_id):
        try:
            result = mongo.db.deleteOne({"user_id": user_id})
            return result
        except Exception as e:
            logging.exception(e)
            return None

    def to_json(self):
        return{
            'user_id': self.user_id,
            'name': self.name,
            'age': self.age
        }
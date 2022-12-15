from app import mongo
from app.models.user_model import User
import logging

class UserService(object):

    @staticmethod
    def create(name, age):
        try:
            newUser = User(name, age)
            result = newUser.create()
            return result
        except Exception as e:
            logging.exception(e)
            return False

    @staticmethod
    def get_list():
        try:
            users = User.getList()
            return users
        except Exception as e:
            logging.exception(e)
            return False

    @staticmethod
    def update(user):
        try:
            result = User.update(user)
            return result
        except Exception as e:
            logging.exception(e)
            return False

    @staticmethod
    def delete(user_id):
        try:
            result = User.delete(user_id)
            return result
        except Exception as e:
            logging.exception(e)
            return False
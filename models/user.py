from mongoorm import MongoORM
import re
from pprint import pprint

class User:
    """
    """
    def __init__(self, credentials={}):
        self.collection = MongoORM(**credentials).case_collection('users')
        

    def get_user_by_atribute(self, **kwargs):
        coursor = self.collection.find_one(kwargs)
        for key in coursor:
            self.__dict__[key] = coursor[key]
    
    
    def get_list_all_users(self):
        coursor = self.collection.find({})
        list_users = []
        for key in coursor:
            del(key["_id"])
            list_users.append(key)
        return list_users


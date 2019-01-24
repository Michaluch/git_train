# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pprint import pprint

class MongoORM(object):
    def __init__(self, **kwargs):
        """
        Initialisator of mongo object
        """
        self.db_host = kwargs.get("host")
        self.db_name = kwargs.get("db")
        self.db_port = kwargs.get("port")
        self.db_user = kwargs.get("user")
        self.db_password = kwargs.get("password")


        def _mongo_url_builder(self):
            url = "mongodb://{0}:{1}@{2}:{3}/{4}".format(self.db_user,
                    self.db_password,
                    self.db_host,
                    self.db_port,
                    self.db_name)
            return url


        def connect_to_db(self):
            """connect to MongoDB database
            """
            try:
                db = MongoClient(host=self._mongo_url_builder())
                return db[self.db_name]
            except:
                return "Cannot conect to db {}".format(self.db_name)

        def case_collection(self, collection=None):
            """Swith on collection in MongoDB database
            """
            try:
                return self.connect_to_db()[collection]
            except:
                return "Cannot switch on collection {}".format(self.collection)

        def select_all(self, collection):
            """db.collection.find()    
            """
            try:
                cursor = self.case_collection(collection).find()
                json_doc = []
                for key in cursor:
                    del(key['_id'])
                    json_doc.append(key)
                return json_doc
            except:
                print "cannot select"


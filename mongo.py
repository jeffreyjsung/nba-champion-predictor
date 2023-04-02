import pymongo

class MongoDBAgent:
    name = "MongoDBAgent"

    def __init__(self, con_string: str, db: str):
        self.__client = pymongo.MongoClient(con_string)
        self.__db = self.__client[db]
        self.__connect_db()


    def __connect_db(self):
        self.__client.server_info()


    def find(self, collection_name: str, query: dict, count=False):
        collection = self.__db[collection_name]
        documents = collection.find(query)
        if count: return collection.count_documents(query)
        if collection.count_documents(query) == 0: return None
        return documents


    def insert_one(self, collection_name: str, data: dict):
        collection = self.__db[collection_name]
        return_statement = collection.insert_one(data)


    def update_one(self, collection_name: str, query: dict, data):
        collection = self.__db[collection_name]
        collection.update_one(filter=query, update=data) 
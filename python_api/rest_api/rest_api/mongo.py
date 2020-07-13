from pymongo import MongoClient

class MongoDB():
    def __init__(self, server, dbName, collectionName):
        self.Client = MongoClient(server)
        self.Db = self.Client.get_database(dbName)
        self.Collection = self.Db.get_collection(collectionName)

if __name__ == "__main__":
    db = MongoDB('127.0.0.1', 'local','startup_log')
    for item in db.Collection.find({}):
        print(item['hostname'])

class DataDao:

    def __init__(self, client, collection_name):
        db = client.Bot
        self.collection = db[collection_name]

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def delete_by_id(self, id):
        return self.collection.delete_one({"_id": id})

    def find_one_by_id(self, id):
        return self.collection.find_one({"_id": id})

    def update(self, update_object):
        return self.collection.update_one(update_object)

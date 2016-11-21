

class DataDao:

    def __init__(self, client):
        self.collection = client.data

    def test_insert(self, data):
        self.collection.insert(data)

    def test_delete_by_id(self):
        print('')

    def test_find(self):
        print('')

    def test_update(self):
        print('')

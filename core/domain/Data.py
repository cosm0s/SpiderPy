
class Data:

    def __init__(self, root, data_type, data):
        self.root = root
        self.data_type = data_type
        self.data = data

    def to_db_collection(self):
        return {
            "root": self.root,
            "type": self.data_type,
            "data": self.data,
        }

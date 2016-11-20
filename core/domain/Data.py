
class Data:

    def __init__(self, root, type, data):
        self.root = root
        self.type = type
        self.data = data

    def to_DB_collection(self):
        return {
            "root":self.root,
            "type":self.type,
            "data": self.data,
        }

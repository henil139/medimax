from app.core.database import db

class ProductDAL:
    def __init__(self):
        self.collection = db["products"]

    def create(self, data: dict):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_all(self):
        # return all documents without _id for now (easy)
        return list(self.collection.find({}, {"_id": 0}))

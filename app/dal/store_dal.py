from app.core.database import db

class StoreDAL:
    def __init__(self):
        self.collection = db["stores"]

    def create(self, data: dict):
        self.collection.insert_one(data)

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_id(self, store_id: str):
        return self.collection.find_one(
            {"store_id": store_id},
            {"_id": 0}
        )

    def update(self, store_id: str, data: dict):
        result = self.collection.update_one(
            {"store_id": store_id},
            {"$set": data}
        )
        return result.matched_count

    def soft_delete(self, store_id: str):
        result = self.collection.update_one(
            {"store_id": store_id},
            {"$set": {"is_active": False}}
        )
        return result.matched_count

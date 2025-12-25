from app.core.database import db
from app.dal.counter_dal import CounterDAL

class BatchDAL:
    def __init__(self):
        self.collection = db["batches"]
        self.counter_dal = CounterDAL()

    def create(self, data: dict) -> str:
        seq = self.counter_dal.get_next_sequence("batch_id")
        batch_id = f"BAT{seq:04d}"

        data["batch_id"] = batch_id
        self.collection.insert_one(data)
        return batch_id

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_id(self, batch_id: str):
        return self.collection.find_one(
            {"batch_id": batch_id},
            {"_id": 0}
        )

    def update(self, batch_id: str, data: dict):
        return self.collection.update_one(
            {"batch_id": batch_id},
            {"$set": data}
        ).matched_count

    def delete(self, batch_id: str):
        return self.collection.delete_one(
            {"batch_id": batch_id}
        ).deleted_count

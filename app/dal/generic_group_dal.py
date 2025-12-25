from app.core.database import db
from app.dal.counter_dal import CounterDAL

class GenericGroupDAL:
    def __init__(self):
        self.collection = db["generic_groups"]
        self.counter_dal = CounterDAL()

    def create(self, data: dict) -> str:
        seq = self.counter_dal.get_next_sequence("generic_group_id")
        group_id = f"GEN{seq:04d}"

        data["generic_group_id"] = group_id
        self.collection.insert_one(data)
        return group_id

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_id(self, group_id: str):
        return self.collection.find_one(
            {"generic_group_id": group_id},
            {"_id": 0}
        )

    def update(self, group_id: str, data: dict):
        return self.collection.update_one(
            {"generic_group_id": group_id},
            {"$set": data}
        ).matched_count

    def delete(self, group_id: str):
        return self.collection.delete_one(
            {"generic_group_id": group_id}
        ).deleted_count

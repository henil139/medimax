from datetime import datetime
from app.core.database import db
from app.dal.counter_dal import CounterDAL

class InventoryDAL:
    def __init__(self):
        self.collection = db["inventory"]
        self.counter_dal = CounterDAL()

    def create(self, data: dict) -> str:
        seq = self.counter_dal.get_next_sequence("inventory_id")
        inventory_id = f"INV{seq:04d}"

        data["inventory_id"] = inventory_id
        data["last_updated"] = datetime.utcnow()

        self.collection.insert_one(data)
        return inventory_id

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_id(self, inventory_id: str):
        return self.collection.find_one(
            {"inventory_id": inventory_id},
            {"_id": 0}
        )

    def update(self, inventory_id: str, quantity: int):
        result = self.collection.update_one(
            {"inventory_id": inventory_id},
            {
                "$set": {
                    "quantity": quantity,
                    "last_updated": datetime.utcnow()
                }
            }
        )
        return result.matched_count

    def delete(self, inventory_id: str):
        return self.collection.delete_one(
            {"inventory_id": inventory_id}
        ).deleted_count

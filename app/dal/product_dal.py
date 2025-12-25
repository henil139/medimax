from app.core.database import db
from app.dal.counter_dal import CounterDAL

class ProductDAL:
    def __init__(self):
        self.collection = db["products"]
        self.counter_dal = CounterDAL()

    def create(self, data: dict) -> str:
        seq = self.counter_dal.get_next_sequence("product_id")
        product_id = f"PRD{seq:04d}"

        data["product_id"] = product_id
        data["is_active"] = True

        self.collection.insert_one(data)
        return product_id

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_id(self, product_id: str):
        return self.collection.find_one(
            {"product_id": product_id},
            {"_id": 0}
        )

    def update(self, product_id: str, data: dict):
        return self.collection.update_one(
            {"product_id": product_id},
            {"$set": data}
        ).matched_count

    def soft_delete(self, product_id: str):
        return self.collection.update_one(
            {"product_id": product_id},
            {"$set": {"is_active": False}}
        ).matched_count

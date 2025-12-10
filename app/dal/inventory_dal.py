from app.core.database import db

class InventoryDAL:
    def __init__(self):
        self.collection = db["inventory"]

    def add_stock(self, product_id: str, quantity: int):
        self.collection.update_one(
            {"product_id": product_id},
            {"$inc": {"quantity": quantity}},
            upsert=True
        )

    def get_stock(self, product_id: str):
        doc = self.collection.find_one({"product_id": product_id}, {"_id": 0})
        return doc or {"product_id": product_id, "quantity": 0}

from app.core.database import db


class InventoryDAL:
    def __init__(self):
        self.collection = db["inventory"]
        self.counter = db["counters"]  # shared collection for number sequences

    def _get_next_inventory_id(self):
        result = self.counter.find_one_and_update(
            {"_id": "inventory"},
            {"$inc": {"sequence": 1}},
            upsert=True,
            return_document=True
        )
        seq = result["sequence"]
        return f"INV{seq:05d}"  # INV00001

    def create(self, product_id: str, quantity: int):
        inv_id = self._get_next_inventory_id()

        doc = {
            "inventory_id": inv_id,
            "product_id": product_id,
            "quantity": quantity
        }

        self.collection.insert_one(doc)
        return inv_id

    def get_by_product(self, product_id: str):
        return self.collection.find_one(
            {"product_id": product_id},
            {"_id": 0}
        )

    def update(self, product_id: str, update_data: dict):
        update_data = {k: v for k, v in update_data.items() if v is not None}

        result = self.collection.update_one(
            {"product_id": product_id},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            return None

        return self.get_by_product(product_id)

    def delete(self, product_id: str):
        result = self.collection.delete_one({"product_id": product_id})
        return result.deleted_count > 0

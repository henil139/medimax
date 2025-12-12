from app.core.database import db

class ProductDAL:
    def __init__(self):
        self.collection = db["products"]

    def create(self, data: dict):
        result = self.collection.insert_one(data)
        return data["product_id"]

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def get_by_id(self, product_id: str):
        return self.collection.find_one({"product_id": product_id}, {"_id": 0})

    def update_product(self, product_id: str, update_data: dict):
        # Remove None fields
        update_data = {k: v for k, v in update_data.items() if v is not None}

        result = self.collection.update_one(
            {"product_id": product_id},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            return None  # Not found

        # return updated product
        return self.get_by_id(product_id)

    def delete_product(self, product_id: str):
        result = self.collection.delete_one({"product_id": product_id})
        return result.deleted_count > 0

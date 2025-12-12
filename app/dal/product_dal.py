from app.core.database import db

class ProductDAL:
    def __init__(self):
        self.collection = db["products"]
        self.counters = db["counters"]

    def _get_next_product_id(self):
        """
        Atomically increments the product counter and returns a new product ID like PRD0001.
        """
        result = self.counters.find_one_and_update(
            {"_id": "product_id"},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=True
        )

        seq_num = result["seq"]
        return f"PRD{seq_num:04d}"  # Formats 1 → PRD0001

    def create(self, data: dict):
        # Insert auto-generated product_id
        data["product_id"] = self._get_next_product_id()

        self.collection.insert_one(data)
        return data["product_id"]  # Return business ID instead of Mongo ObjectId

    def get_all(self):
        # Exclude MongoDB internal _id and return clean data
        return list(self.collection.find({}, {"_id": 0}))

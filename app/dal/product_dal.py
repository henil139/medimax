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

    def generic_suggestions(self, generic_group_id: str, store_id: str):
        pipeline = [
            {
                "$match": {
                    "generic_group_id": generic_group_id,
                    "is_active": True
                }
            },
            {
                "$lookup": {
                    "from": "batches",
                    "localField": "product_id",
                    "foreignField": "product_id",
                    "as": "batches"
                }
            },
            {"$unwind": "$batches"},
            {
                "$lookup": {
                    "from": "inventory",
                    "let": {"batch_id": "$batches.batch_id"},
                    "pipeline": [
                        {
                            "$match": {
                                "$expr": {
                                    "$and": [
                                        {"$eq": ["$batch_id", "$$batch_id"]},
                                        {"$eq": ["$store_id", store_id]},
                                        {"$gt": ["$quantity", 0]}
                                    ]
                                }
                            }
                        }
                    ],
                    "as": "inventory"
                }
            },
            {"$match": {"inventory": {"$ne": []}}},
            {
                "$group": {
                    "_id": "$product_id",
                    "name": {"$first": "$name"},
                    "manufacturer": {"$first": "$manufacturer"},
                    "mrp": {"$first": "$mrp"},
                    "pack_size": {"$first": "$pack_size"},
                    "is_assured": {"$first": "$is_assured"},
                    "total_quantity": {
                        "$sum": {"$arrayElemAt": ["$inventory.quantity", 0]}
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "product_id": "$_id",
                    "name": 1,
                    "manufacturer": 1,
                    "mrp": 1,
                    "pack_size": 1,
                    "is_assured": 1,
                    "total_quantity": 1
                }
            }
        ]

        return list(self.collection.aggregate(pipeline))

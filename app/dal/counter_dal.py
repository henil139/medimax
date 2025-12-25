from app.core.database import db

class CounterDAL:
    def __init__(self):
        self.collection = db["counters"]

    def get_next_sequence(self, name: str) -> int:
        counter = self.collection.find_one_and_update(
            {"_id": name},
            {"$inc": {"sequence": 1}},
            upsert=True,
            return_document=True
        )
        return counter["sequence"]

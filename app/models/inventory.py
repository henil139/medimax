from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InventoryBase(BaseModel):
    store_id: str
    batch_id: str
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    quantity: Optional[int] = None

class InventoryResponse(InventoryBase):
    inventory_id: str
    last_updated: datetime

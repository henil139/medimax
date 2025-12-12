from pydantic import BaseModel
from typing import Optional

class InventoryCreate(BaseModel):
    product_id: str
    quantity: int

class InventoryUpdate(BaseModel):
    quantity: Optional[int] = None

class InventoryResponse(BaseModel):
    inventory_id: str
    product_id: str
    quantity: int

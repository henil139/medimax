from pydantic import BaseModel

class InventoryUpdate(BaseModel):
    product_id: str
    quantity: int

class InventoryResponse(BaseModel):
    product_id: str
    quantity: int

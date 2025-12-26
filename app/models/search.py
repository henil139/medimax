from pydantic import BaseModel

class StoreProductSearchResponse(BaseModel):
    product_id: str
    name: str
    manufacturer: str
    mrp: float
    is_assured: bool
    total_quantity: int

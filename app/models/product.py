from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    manufacturer: str
    mrp: float


class ProductResponse(BaseModel):
    product_id: str
    name: str
    manufacturer: str
    mrp: float

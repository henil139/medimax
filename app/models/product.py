from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    manufacturer: str
    mrp: float

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    mrp: Optional[float] = None

class ProductResponse(BaseModel):
    product_id: str
    name: str
    manufacturer: str
    mrp: float

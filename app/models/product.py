from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    manufacturer: str
    mrp: float

class ProductResponse(BaseModel):
    name: str
    manufacturer: str
    mrp: float

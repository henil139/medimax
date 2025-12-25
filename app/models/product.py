from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    manufacturer: str
    mrp: float
    pack_size: str
    type: str
    category_ids: List[str]
    generic_group_id: Optional[str] = None
    is_assured: bool = False

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    mrp: Optional[float] = None
    pack_size: Optional[str] = None
    category_ids: Optional[List[str]] = None
    generic_group_id: Optional[str] = None
    is_assured: Optional[bool] = None
    is_active: Optional[bool] = None

class ProductResponse(ProductBase):
    product_id: str
    is_active: bool

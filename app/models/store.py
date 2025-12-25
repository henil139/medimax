from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class StoreBase(BaseModel):
    name: str
    address: str
    contact_number: str
    region_id: str

class StoreCreate(StoreBase):
    store_id: str
    opened_on: datetime
    is_active: bool = True

class StoreUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[str] = None
    region_id: Optional[str] = None
    is_active: Optional[bool] = None

class StoreResponse(StoreCreate):
    pass

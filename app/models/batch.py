from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BatchBase(BaseModel):
    product_id: str
    batch_number: str
    manufactured_on: datetime
    expiry_date: datetime
    mrp: float

class BatchCreate(BatchBase):
    pass

class BatchUpdate(BaseModel):
    batch_number: Optional[str] = None
    manufactured_on: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    mrp: Optional[float] = None

class BatchResponse(BatchBase):
    batch_id: str

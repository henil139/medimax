from pydantic import BaseModel
from typing import Optional

class GenericGroupBase(BaseModel):
    name: str
    description: str

class GenericGroupCreate(GenericGroupBase):
    pass

class GenericGroupUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class GenericGroupResponse(GenericGroupBase):
    generic_group_id: str

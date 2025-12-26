from pydantic import BaseModel

class GenericSuggestionResponse(BaseModel):
    product_id: str
    name: str
    manufacturer: str
    mrp: float
    is_assured: bool
    total_quantity: int

from fastapi import APIRouter, Query
from typing import List
from app.dal.inventory_dal import InventoryDAL
from app.models.generic_suggestion import GenericSuggestionResponse

router = APIRouter(
    prefix="/generics",
    tags=["Generic Suggestions"]
)

inventory_dal = InventoryDAL()

@router.get(
    "/suggestions",
    response_model=List[GenericSuggestionResponse]
)
def generic_suggestions(
    store_id: str = Query(...),
    generic_group_id: str = Query(...)
):
    return inventory_dal.generic_suggestions(
        store_id=store_id,
        generic_group_id=generic_group_id
    )

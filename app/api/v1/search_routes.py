from fastapi import APIRouter, Query
from app.dal.inventory_dal import InventoryDAL
from app.models.search import StoreProductSearchResponse
from typing import List

router = APIRouter(prefix="/search", tags=["Search"])

inventory_dal = InventoryDAL()

@router.get(
    "/products",
    response_model=List[StoreProductSearchResponse]
)
def search_products(
    store_id: str = Query(...),
    q: str = Query(...)
):
    return inventory_dal.search_products_in_store(
        store_id=store_id,
        search_text=q
    )

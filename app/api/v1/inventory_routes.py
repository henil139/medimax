from fastapi import APIRouter
from app.dal.inventory_dal import InventoryDAL
from app.models.inventory import InventoryUpdate, InventoryResponse

router = APIRouter(prefix="/inventory", tags=["Inventory"])

inventory_dal = InventoryDAL()

@router.post("/", response_model=dict)
def update_inventory(payload: InventoryUpdate):
    inventory_dal.add_stock(payload.product_id, payload.quantity)
    return {"status": "stock updated"}

@router.get("/{product_id}", response_model=InventoryResponse)
def get_stock(product_id: str):
    return inventory_dal.get_stock(product_id)

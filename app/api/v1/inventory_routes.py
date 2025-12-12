from fastapi import APIRouter, HTTPException
from app.dal.inventory_dal import InventoryDAL
from app.models.inventory import InventoryCreate, InventoryUpdate, InventoryResponse

router = APIRouter(prefix="/inventory", tags=["Inventory"])
inv_dal = InventoryDAL()

@router.post("/", response_model=dict)
def create_inventory(data: InventoryCreate):
    inv_id = inv_dal.create(data.product_id, data.quantity)
    return {"inventory_id": inv_id}

@router.get("/{product_id}", response_model=InventoryResponse)
def get_inventory(product_id: str):
    inv = inv_dal.get_by_product(product_id)
    if inv is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inv

@router.put("/{product_id}", response_model=InventoryResponse)
def update_inventory(product_id: str, updates: InventoryUpdate):
    inv = inv_dal.update(product_id, updates.model_dump())
    if inv is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inv

@router.delete("/{product_id}", status_code=204)
def delete_inventory(product_id: str):
    success = inv_dal.delete(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return None

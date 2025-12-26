from fastapi import APIRouter, HTTPException
from app.dal.inventory_dal import InventoryDAL
from app.models.inventory import (
    InventoryCreate,
    InventoryUpdate,
    InventoryResponse
)

router = APIRouter(prefix="/inventory", tags=["Inventory"])
inventory_dal = InventoryDAL()

@router.post("/", status_code=201)
def create_inventory(item: InventoryCreate):
    inventory_id = inventory_dal.create(item.model_dump())
    return {"inventory_id": inventory_id}

@router.get("/", response_model=list[InventoryResponse])
def get_inventory():
    return inventory_dal.get_all()

@router.get("/{inventory_id}", response_model=InventoryResponse)
def get_inventory_item(inventory_id: str):
    item = inventory_dal.get_by_id(inventory_id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item

@router.put("/{inventory_id}")
def update_inventory(inventory_id: str, item: InventoryUpdate):
    if item.quantity is None:
        raise HTTPException(status_code=400, detail="Quantity required")

    updated = inventory_dal.update(inventory_id, item.quantity)
    if updated == 0:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return {"message": "Inventory updated"}

@router.delete("/{inventory_id}")
def delete_inventory(inventory_id: str):
    deleted = inventory_dal.delete(inventory_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return {"message": "Inventory deleted"}

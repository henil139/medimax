from fastapi import APIRouter, HTTPException
from app.dal.store_dal import StoreDAL
from app.models.store import (
    StoreCreate,
    StoreUpdate,
    StoreResponse
)

router = APIRouter(prefix="/stores", tags=["Stores"])
store_dal = StoreDAL()

# CREATE
@router.post("/", status_code=201)
def create_store(store: StoreCreate):
    store_dal.create(store.model_dump())
    return {"message": "Store created successfully"}

# READ ALL
@router.get("/", response_model=list[StoreResponse])
def get_stores():
    return store_dal.get_all()

# READ ONE
@router.get("/{store_id}", response_model=StoreResponse)
def get_store(store_id: str):
    store = store_dal.get_by_id(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

# UPDATE
@router.put("/{store_id}")
def update_store(store_id: str, store: StoreUpdate):
    updated = store_dal.update(
        store_id,
        store.model_dump(exclude_unset=True)
    )
    if updated == 0:
        raise HTTPException(status_code=404, detail="Store not found")
    return {"message": "Store updated successfully"}

# DELETE (soft delete)
@router.delete("/{store_id}")
def delete_store(store_id: str):
    deleted = store_dal.soft_delete(store_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Store not found")
    return {"message": "Store deactivated successfully"}

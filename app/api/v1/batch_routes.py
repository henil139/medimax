from fastapi import APIRouter, HTTPException
from app.dal.batch_dal import BatchDAL
from app.models.batch import (
    BatchCreate,
    BatchUpdate,
    BatchResponse
)

router = APIRouter(prefix="/batches", tags=["Batches"])
batch_dal = BatchDAL()

@router.post("/", status_code=201)
def create_batch(batch: BatchCreate):
    batch_id = batch_dal.create(batch.model_dump())
    return {"batch_id": batch_id}

@router.get("/", response_model=list[BatchResponse])
def get_batches():
    return batch_dal.get_all()

@router.get("/{batch_id}", response_model=BatchResponse)
def get_batch(batch_id: str):
    batch = batch_dal.get_by_id(batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch

@router.put("/{batch_id}")
def update_batch(batch_id: str, batch: BatchUpdate):
    updated = batch_dal.update(
        batch_id,
        batch.model_dump(exclude_unset=True)
    )
    if updated == 0:
        raise HTTPException(status_code=404, detail="Batch not found")
    return {"message": "Batch updated"}

@router.delete("/{batch_id}")
def delete_batch(batch_id: str):
    deleted = batch_dal.delete(batch_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Batch not found")
    return {"message": "Batch deleted"}

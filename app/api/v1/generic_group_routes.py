from fastapi import APIRouter, HTTPException
from app.dal.generic_group_dal import GenericGroupDAL
from app.models.generic_group import (
    GenericGroupCreate,
    GenericGroupUpdate,
    GenericGroupResponse
)

router = APIRouter(prefix="/generic-groups", tags=["Generic Groups"])
group_dal = GenericGroupDAL()

@router.post("/", status_code=201)
def create_group(group: GenericGroupCreate):
    group_id = group_dal.create(group.model_dump())
    return {"generic_group_id": group_id}

@router.get("/", response_model=list[GenericGroupResponse])
def get_groups():
    return group_dal.get_all()

@router.get("/{group_id}", response_model=GenericGroupResponse)
def get_group(group_id: str):
    group = group_dal.get_by_id(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Generic group not found")
    return group

@router.put("/{group_id}")
def update_group(group_id: str, group: GenericGroupUpdate):
    updated = group_dal.update(
        group_id,
        group.model_dump(exclude_unset=True)
    )
    if updated == 0:
        raise HTTPException(status_code=404, detail="Generic group not found")
    return {"message": "Generic group updated"}

@router.delete("/{group_id}")
def delete_group(group_id: str):
    deleted = group_dal.delete(group_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Generic group not found")
    return {"message": "Generic group deleted"}

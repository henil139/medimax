from fastapi import APIRouter, HTTPException, Query
from app.dal.product_dal import ProductDAL
from app.models.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

router = APIRouter(prefix="/products", tags=["Products"])
product_dal = ProductDAL()

@router.post("/", status_code=201)
def create_product(product: ProductCreate):
    product_id = product_dal.create(product.model_dump())
    return {"product_id": product_id}

@router.get("/", response_model=list[ProductResponse])
def get_products():
    return product_dal.get_all()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: str):
    product = product_dal.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}")
def update_product(product_id: str, product: ProductUpdate):
    updated = product_dal.update(
        product_id,
        product.model_dump(exclude_unset=True)
    )
    if updated == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated"}

@router.delete("/{product_id}")
def delete_product(product_id: str):
    deleted = product_dal.soft_delete(product_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deactivated"}

@router.get("/suggestions/generic")
def get_generic_suggestions(
    generic_group_id: str = Query(..., example="GEN0001"),
    store_id: str = Query(..., example="STR001")
):
    return product_dal.generic_suggestions(
        generic_group_id=generic_group_id,
        store_id=store_id
    )
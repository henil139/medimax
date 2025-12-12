from fastapi import APIRouter, HTTPException
from app.dal.product_dal import ProductDAL
from app.models.product import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])

product_dal = ProductDAL()

@router.post("/", response_model=dict)
def create_product(product: ProductCreate):
    product_dict = product.model_dump()
    inserted_id = product_dal.create(product_dict)
    return {"product_id": inserted_id}


@router.get("/", response_model=list[ProductResponse])
def get_products():
    return product_dal.get_all()


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: str, updates: ProductUpdate):
    updated = product_dal.update_product(product_id, updates.model_dump())

    if updated is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: str):
    success = product_dal.delete_product(product_id)

    if not success:
        raise HTTPException(status_code=404, detail="Product not found")

    return None

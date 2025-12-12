from fastapi import APIRouter
from app.dal.product_dal import ProductDAL
from app.models.product import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])
product_dal = ProductDAL()

@router.post("/", response_model=dict)
def create_product(product: ProductCreate):
    product_dict = product.model_dump()
    product_id = product_dal.create(product_dict)
    return {"product_id": product_id}


@router.get("/", response_model=list[ProductResponse])
def get_products():
    return product_dal.get_all()

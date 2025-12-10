from fastapi import APIRouter
from app.dal.product_dal import ProductDAL
from app.dal.inventory_dal import InventoryDAL

router = APIRouter()

product_dal = ProductDAL()
inventory_dal = InventoryDAL()

@router.post("/add-product")
def add_product(name: str, manufacturer: str, mrp: float):
    product = {
        "name": name,
        "manufacturer": manufacturer,
        "mrp": mrp
    }
    pid = product_dal.create(product)
    return {"inserted_id": pid}

@router.get("/get-products")
def get_products():
    return product_dal.get_all()

@router.post("/add-stock")
def add_stock(product_id: str, quantity: int):
    inventory_dal.add_stock(product_id, quantity)
    return {"status": "stock updated"}

@router.get("/get-stock")
def get_stock(product_id: str):
    return inventory_dal.get_stock(product_id)

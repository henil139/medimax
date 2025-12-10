from fastapi import FastAPI
from app.api.v1.product_routes import router as product_router
from app.api.v1.inventory_routes import router as inventory_router
from app.api.v1.db_test import router as db_test_router

app = FastAPI()

app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(db_test_router)

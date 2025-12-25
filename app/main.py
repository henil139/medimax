from fastapi import FastAPI
from app.api.v1.product_routes import router as product_router
from app.api.v1.inventory_routes import router as inventory_router
from app.api.v1.db_test import router as db_test_router
from app.api.v1.store_routes import router as store_router
from app.api.v1.generic_group_routes import router as generic_group_router
from app.api.v1.batch_routes import router as batch_router


app = FastAPI()

app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(db_test_router)

app.include_router(store_router)

app.include_router(generic_group_router)

app.include_router(batch_router)
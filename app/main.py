from fastapi import FastAPI
from app.api.v1.product_routes import router as product_router
from app.api.v1.inventory_routes import router as inventory_router
from app.api.v1.db_test import router as db_test_router
from app.api.v1.store_routes import router as store_router
from app.api.v1.generic_group_routes import router as generic_group_router
from app.api.v1.batch_routes import router as batch_router
from app.api.v1.search_routes import router as search_router
from app.api.v1.generic_routes import router as generic_router
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()

app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(db_test_router)

app.include_router(store_router)

app.include_router(generic_group_router)

app.include_router(batch_router)

app.include_router(search_router)

app.include_router(generic_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://a1f96ac3-9f25-4814-ac9b-56e616ac75e7.lovableproject.com", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI
from app.api.v1.db_test import router as db_test_router

app = FastAPI()

app.include_router(db_test_router)

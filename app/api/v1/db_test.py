from fastapi import APIRouter
from app.core.database import db

router = APIRouter()

@router.get("/db-test")
def test_db():
    try:
        collections = db.list_collection_names()
        return {"status": "connected", "collections": collections}
    except Exception as e:
        return {"status": "error", "message": str(e)}

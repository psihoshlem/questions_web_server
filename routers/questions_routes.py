from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import FileResponse

from db_functions import write_question, get_last_question

router = APIRouter()

@router.get("/get_all_products", tags=["products"])
async def get_all_products_info():
    return write_question()
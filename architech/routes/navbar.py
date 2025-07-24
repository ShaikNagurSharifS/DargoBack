from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

def get_navbar_items_list():
    # Example implementation, replace with your actual logic
    return {"items": ["Home", "About", "Services","Projects","Portfolio", "Contact"]}



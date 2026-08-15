from app.controllers import book_controller as controller
from fastapi import APIRouter

router = APIRouter(prefix="/api/books", tags=["Books"])

@router.post("/")
async def add_book(book: dict):
 return  controller.create_book(book)
@router.get("/")
async def get_books():
 return controller.get_books();
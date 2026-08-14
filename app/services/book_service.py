from app.repositories import book_repository as repository
import uuid
from datetime import datetime

def create(book):
    book["id"] = uuid.uuid4()
    book["CreatedAt"] = datetime.now()
    return  repository.save(book)
    
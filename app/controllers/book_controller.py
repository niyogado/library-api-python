from app.services import book_service as service

def create_book(book):
    try:
        return  service.create(book)

    except Exception as e:
        return {
            "Message":"Something unexpected happens",
            "Error": str(e),
        }
def get_books():
    return service.get_all()
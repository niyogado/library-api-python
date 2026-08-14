from app.store import in_memory_store as store
books = store.books
def save(book):
    books.append(book)
    return book
       
 

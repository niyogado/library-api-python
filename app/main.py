from fastapi import FastAPI
from app.routes.book_routes import router

app = FastAPI(
    title="Library API",
    version="1.0.0"
)


app.include_router(router)

@app.get("/")
def home():
    return {
        "Message":"Welcome to library API"
    }
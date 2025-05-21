from fastapi import FastAPI, HTTPException
from models import Book
from crud import create_book, get_all_books, get_book_by_id, delete_book

app = FastAPI()

@app.post("/books/")
async def add_book(book: Book):
    book_id = await create_book(book)
    return {"id": book_id}

@app.get("/books/")
async def list_books():
    return await get_all_books()

@app.get("/books/{book_id}")
async def get_book(book_id: str):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{book_id}")
async def remove_book(book_id: str):
    deleted = await delete_book(book_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"status": "deleted"}

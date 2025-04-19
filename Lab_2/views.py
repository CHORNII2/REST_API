from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str

class BookCreate(BaseModel):
    title: str
    author: str

books: List[Book] = []
next_id = 1

@app.get("/books", response_model=List[Book])
async def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=Book, status_code=201)
async def add_book(book_data: BookCreate):
    global next_id
    book = Book(id=next_id, **book_data.dict())
    books.append(book)
    next_id += 1
    return book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    global books
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    books = [b for b in books if b.id != book_id]
    return {"message": "Book deleted"}

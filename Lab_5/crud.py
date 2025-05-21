from models import Book
from database import collection
from bson import ObjectId
from pydantic_mongo import PydanticObjectId

async def create_book(book: Book):
    result = await collection.insert_one(book.dict(by_alias=True, exclude={"id"}))
    return str(result.inserted_id)

async def get_all_books():
    books = []
    cursor = collection.find({})
    async for document in cursor:
        books.append(Book(**document))
    return books

async def get_book_by_id(book_id: str):
    book = await collection.find_one({"_id": PydanticObjectId(book_id)})
    if book:
        return Book(**book)

async def delete_book(book_id: str):
    result = await collection.delete_one({"_id": PydanticObjectId(book_id)})
    return result.deleted_count

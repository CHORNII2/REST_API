from flask_restful import Resource, reqparse
from db import collection
from models import book_serializer
from bson import ObjectId

parser = reqparse.RequestParser()
parser.add_argument("title", required=True)
parser.add_argument("author", required=True)
parser.add_argument("year", type=int, required=True)

class BookList(Resource):
    def get(self):
        books = collection.find()
        return [book_serializer(book) for book in books]

    def post(self):
        args = parser.parse_args()
        result = collection.insert_one(args)
        return {"id": str(result.inserted_id)}, 201

class Book(Resource):
    def get(self, book_id):
        book = collection.find_one({"_id": ObjectId(book_id)})
        if book:
            return book_serializer(book)
        return {"message": "Book not found"}, 404

    def delete(self, book_id):
        result = collection.delete_one({"_id": ObjectId(book_id)})
        if result.deleted_count == 1:
            return {"message": "Book deleted"}
        return {"message": "Book not found"}, 404

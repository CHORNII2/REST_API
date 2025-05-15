from flask import request, jsonify, abort
from app import app, db
from app.models import Book
from app.schemas import book_schema, books_schema


@app.route("/books", methods=["GET"])
def get_books():
    limit = request.args.get('limit', default=10, type=int)
    after_id = request.args.get('after_id', default=0, type=int) 

    books = Book.query.filter(Book.id > after_id).order_by(Book.id).limit(limit).all()

    return books_schema.jsonify(books)


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return book_schema.jsonify(book)


@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    errors = book_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    book = Book(title=data['title'], author=data['author'])
    db.session.add(book)
    db.session.commit()
    return book_schema.jsonify(book), 201


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})

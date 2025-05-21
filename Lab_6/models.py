def book_serializer(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "year": book["year"]
    }

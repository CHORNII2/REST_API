from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from resources import BookList, Book

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

api.add_resource(BookList, "/books", endpoint="books")
api.add_resource(Book, "/books/<string:book_id>", endpoint="book")

@app.route('/')
def docs_redirect():
    return "<p>Go to <a href='/apidocs'>Swagger UI</a></p>"

if __name__ == "__main__":
    app.run(debug=True)

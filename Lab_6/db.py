from pymongo import MongoClient

client = MongoClient("mongodb://mongo_admin:password@localhost:27017")
db = client.books
collection = db["books"]

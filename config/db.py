from pymongo import MongoClient

MONGO_URI = "mongodb+srv://<username>:<password>@fastapitutorial.o8k580l.mongodb.net/notes"

conn = MongoClient(MONGO_URI)
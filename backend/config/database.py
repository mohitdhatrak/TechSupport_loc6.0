from pymongo import MongoClient
client = MongoClient('mongodb+srv://admin:v74qzvqYkKv4H5Ob@cluster0.xb5bzyx.mongodb.net/')

db = client.todo_db
collection_name = db['todo_collection']
user_collection = db['user_collection'] 
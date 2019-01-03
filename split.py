import pymongo

# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.vairoma # insert the database name you want to connect in [database_name]
collection = db.articles_copy # insert the collection name you want to connect in [collection_name]

# Example 1: get documents which satisfy your conditions
articles = collection.find()

# Example 2: update each document by using for loop

for article in articles:
	id = article['id']
	texts = para.split('\n')

	collection.insert_one({"_id":article['_id']},{"id":article['id']},{"title":article['title']},{"text":text}})

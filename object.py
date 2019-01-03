import pymongo

# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.eduvis # insert the database name you want to connect in [database_name]
collection = db.wiki_collection # insert the collection name you want to connect in [collection_name]
#collection2 = db.articles
# Example 1: get documents which satisfy your conditions
articles = collection.find()
# Example 2: update each document by using for loop

obj = {}
for article in articles:
	para = article['text']
	texts = para.split('\n')

	for i in range(len(texts)):
		obj[str(i)] = texts[i]

	collection.update({"id":article['id']},{"$set":{"text":obj}})

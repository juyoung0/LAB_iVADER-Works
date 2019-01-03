import pymongo

# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.eduvis # insert the database name you want to connect in [database_name]
collection = db.yearCollection # insert the collection name you want to connect in [collection_name]
collection2 = db.locationCollection
# Example 1: get documents which satisfy your conditions
articles = collection.find()

# Example 2: update each document by using for loop
idList = []
for article in articles:
	idList.append(article['_id'])

collection2.aggregate([{"$match": {"_id": {"$in":idList}}},{"$out":'YearLocCollection'}])

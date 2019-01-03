import pymongo
from bson.code import Code
# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.wiki_new # insert the database name you want to connect in [database_name]
collection = db.topiclist # insert the collection name you want to connect in [collection_name]

result = collection.find({})

target = open('topiclist.json', 'w')
target.seek(0)

for doc in result:
	content = str(doc)
	target.write(content)

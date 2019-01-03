import pymongo

# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.wiki_new # insert the database name you want to connect in [database_name]
collection = db.topiclist # insert the collection name you want to connect in [collection_name]
# Example 1: get documents which satisfy your conditions
topics = collection.find()

# Example 2: update each document by using for loop

for topic in topics:
	para = topic['topiclist']
	filename ="result/" + str(topic['topicid']) + ".json"
	target = open(filename, 'w')
	target.seek(0)
	for i in range(len(para)):
		order = "key"+str(para[i]['order'])
		keyword = para[i]['keyword']
		target.write("\""+order + "\"" + ": "+keyword+",\n") 	
#	texts = para.split('\n')
#	texts = article['text']
#	target.write(texts)

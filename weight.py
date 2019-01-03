import pymongo

# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.vairoma # insert the database name you want to connect in [database_name]
collection = db.articles_copy # insert the collection name you want to connect in [collection_name]
dbList = ["topic0", "topic1", "topic2", "topic3", "topic4", "topic5", "topic6", "topic7", "topic8", "topic9", "topic10", "topic11", "topic12", "topic13", "topic14", "topic15", "topic16", "topic17", "topic18", "topic19", "topic20", "topic21", "topic22", "topic23", "topic24", "topic25", "topic26", "topic27", "topic28", "topic29", "topic30", "topic31", "topic32", "topic33", "topic34", "topic35", "topic36", "topic37", "topic38", "topic39"]
wList = ["weight0", "weight1", "weight2", "weight3", "weight4", "weight5", "weight6", "weight7", "weight8", "weight9", "weight10", "weight11", "weight12", "weight13", "weight14", "weight15", "weight16", "weight17", "weight18", "weight19", "weight20", "weight21", "weight22", "weight23", "weight24", "weight25", "weight26", "weight27", "weight28", "weight29", "weight30", "weight31", "weight32", "weight33", "weight34", "weight35", "weight36", "weight37", "weight38", "weight39"]

for i in range(1):
	topic = getattr(db, dbList[i])

#	articles = topic.find()

#	articles.forEach

	topic.aggregate([{"$group":{"_id":"$id","weightlist":{"$push":"$weight"}}},{"$out":wList[i]}])
#	topic.updatemany([{"$group":{"_id":"$id","weightlist":{"$push":{dbList[i] :"$weight"}}}},{"$out":"weights"}])


#        collection.update({"id":"$id","weightlist":{"$addToSet":{"weights":"$weight"}}}, multi=True)
		

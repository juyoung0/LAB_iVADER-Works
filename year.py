import pymongo

# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.eduvis # insert the database name you want to connect in [database_name]
collection = db.wiki_collection # insert the collection name you want to connect in [collection_name]

years = ["" for x in range(117*4)]
j = 1
for i in range(117):
	j=i*4
	years[j+0] = str(i+1900)
	years[j+1] = str(i+1900)+"*"
	years[j+2] = str(i+1900)+"**"
	years[j+3] = str(i+1900)+"***"
	
# Example 1: get documents which satisfy your conditions
#articles = collection.find()
# Example 2: update each document by using for loop
#for article in articles:

#print years 

collection.aggregate([{"$match":{"unique_date":{"$in":years}}},{"$out":'yearCollection'}])
#collection.aggregate([{"$match":{"unique_date":{"$nin":years}}},{"$out":'NotyearCollection'}])




import pymongo
from bson.code import Code
# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.wiki_new # insert the database name you want to connect in [database_name]
collection = db.wiki_collections # insert the collection name you want to connect in [collection_name]


m = Code("function(){emit(this._id, this.articles)}")
r = Code("function(key, values){var result={""articles"":values.articles}; return result;}")

for i in range(1900, 2017):
	year = str(i)
	articles = collection.aggregate([{"$match":{"$or":[{"unique_date": year},{"unique_date":year+"*"},{"unique_date":year+"**"},{"unique_date":year+"***"}]}}, {"$group": {"_id": {"year": year},"articles": {"$push": "$id"}}}, {"$out": year}])
	db[year].map_reduce(m, r, out= {"reduce": 'filteredYear'})
	db[year].drop()

import pymongo

# MongoDB connection
connection = pymongo.MongoClient("localhost", 27017)
db = connection.wiki_new # insert the database name you want to connect in [database_name]
collection = db.topiclist # insert the collection name you want to connect in [collection_name]

f = open('topic.text','r')
print(f)

i = 0;
array = []

for line in f:
	array.append(line.split("topic"+str(i)))
	i = i + 1

for i in range(len(array)-1):
	result = []
	topicList = []
	topicList = array[i][1].split()

	for k in range(len(topicList)):
		result.append({"keyword":topicList[k], "order":k})

	collection.insert_one({"topicid":i,"topicname":"topic"+str(i),"topiclist":result})

f = open("ancientTopic.txt", "r")
target = open("ancient.json", "w")
target.seek(0)
target.write("{\n")
target.write("	\"name\": \"root\",\n")
target.write("	\"radius\": \"40\",\n")
target.write("	\"children\": [\n")


topicNum = 0
result = {}
childeren = []
lines = f.readlines()
for line in lines:
	
	words = line.split(',')
	target.write("	{\n")
	target.write("		\"name\": \"Topic" + str(topicNum) + "\",\n")
	target.write("		\"radius\": \"10\",\n")
	target.write("		\"topicid\": " + str(topicNum) + ",\n")
	target.write("		\"text\": {\n")


	for i in range(len(words)-1):
		if i != 49:
			target.write("			\"key"+str(i)+"\": \"" + words[i+1] + "\",\n")
		if i == 49:
			target.write("			\"key"+str(i)+"\": \"" + words[i+1] + "\"")

	target.write("\n		}\n	},\n")

	topicNum = topicNum + 1


target.write("]\n}")
f.close()
target.close()

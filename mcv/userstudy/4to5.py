import csv
prob = ["Problem 4", "Problem 5"]
group = ["A", "B", "C"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time"]




with open('withoutD.csv', 'rb')as csvfile:
    	firstrow = True
	spamreader = csv.reader(csvfile, delimiter=',')
	rate = [None]*5
	group_num = [None] * 5
	for n in range(5):
		rate[n] = [None] * 4
		group_num[n] = 0
	for i in range(5):
		for h in range(4):
			rate[i][h] = 0
						
	flag = 0
	oo = []
	ox = []
	xo = []
	xx = []
	for row in spamreader:
		
		if firstrow:
			firstrow = False
		else:
			if "Problem 4" == row[0]:
				if row[11] == "1":
					flag = 1
				else:
					flag = 2
			elif "Problem 5" == row[0]:
                                g = ord(row[1])-65
                                group_num[g] += 1

				if flag == 1:
					if row[11] == "1":
						rate[g][0] += 1
						#if row[1] == "C":
						oo.append(row[2])
					else:
						rate[g][1] += 1
						ox.append(row[2])

				elif flag == 2:
                                        if row[11] == "1":
                                                rate[g][2] += 1
						xo.append(row[2])
                                        else:
                                                rate[g][3] += 1
						xx.append(row[2])
				flag = 0



	for i in range(5):	
		print "Group "+chr(i+65) + " : " +str(group_num[i])
		print rate[i]

	print oo
	print ox
	print xo
	print xx
	
			

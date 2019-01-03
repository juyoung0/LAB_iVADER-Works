import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4", "Problem 5"]
group = ["A", "B", "C"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","time","confidence"]

groupN = 3
col = 11

for p in prob:
	with open('modify_time.csv', 'rb')as csvfile:
       		firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		avg_list = [None]*groupN
		group_num = [None]*groupN
		for n in range(groupN):
			avg_list[n] = [None] * col
			group_num[n] = 0
		for i in range(groupN):
			for j in range(col):
				avg_list[i][j] = 0.0
		
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if True :
					if p == row[0]:
        	        	                g = ord(row[1])-65
                        		        group_num[g] += 1
						for j in range(col):
                                        	        if j!=9 : avg_list[g][j] += float(row[j+3])
							else:
                	                                        t = time.strptime(row[j+3],'%H:%M:%S')
                        	                                s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
	                                                        avg_list[g][j] += s

		for m in range(groupN):
			for k in range(col):
				if group_num[m] != 0:
					avg_list[m][k] /= group_num[m]
	#		if p == "Problem 5":
	#		avg_list[m][1] = avg_list[m][0] / avg_list[m][2]
 #                       avg_list[m][13] = avg_list[m][12] / avg_list[m][9]

		for i in range(groupN):
			print "Group "+chr(i+65) + " : " +str(group_num[i])
		
	                for l in range(col):
                        	if l == 9:
                        	        seconds = avg_list[i][l]
                                	minutes = seconds // 60
                       	        	print "%02d:%02d" % (minutes, seconds % 60)
                        	else:
                                	print avg_list[i][l]

	        	speru = avg_list[i][9] / avg_list[i][1]
                	mperu = speru // 60
                	print "%02d:%02d" % (mperu, speru % 60)


import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3"]
group = ["A", "B", "C", "D"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time","sess", "confidence"]


for p in prob:
	with open('3rd.csv', 'rb')as csvfile:
       		firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		avg_list = [None]*4
		group_num = [None]*4
		for n in range(4):
			avg_list[n] = [None] * 12
			group_num[n] = 0
		for i in range(4):
			for j in range(12):
				avg_list[i][j] = 0.0
		
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if p == row[0]:
                	                g = ord(row[1])-65
                        	        group_num[g] += 1
					for j in range(12):
                                                if j == 10:
                                                        t = time.strptime(row[j+3],'%H:%M:%S')
                                                        s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
                                                        avg_list[g][j] += s
                                                else:
							if j == 11:	
								avg_list[g][j] += float(row[j+4])
							else:
								avg_list[g][j] += float(row[j+3])
		for m in range(4):
			for k in range(12):
				if group_num[m] != 0:
					avg_list[m][k] /= group_num[m]

		for i in range(4):
			print "Group "+chr(i+65) + " : " +str(group_num[i])
	

	                for l in range(12):
                        	if l == 10:
                        	        seconds = avg_list[i][l]
                                	minutes = seconds // 60
                       	        	print "%02d:%02d" % (minutes, seconds % 60)
	                       	else:
                               		print avg_list[i][l]


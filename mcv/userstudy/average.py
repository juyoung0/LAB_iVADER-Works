import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4", "Problem 5"]
group = ["A", "B", "C", "D"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time","sess","confidence"]

#number = 49
#number = 88
#number = 103
#number = 15
#number = 97
number = 44
col = 14
for p in prob:
	with open('withoutD_conf.csv', 'rb')as csvfile:
        	firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		avg_list = [None] * col
		for i in range(col):
			avg_list[i] = 0.0
		
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if p == row[0]:
					for j in range(col):
						if j == 0 : avg_list[j] += float(row[j+3])	
						elif j == 1:
							avg_list[j] = 0 
						elif j == 11:
							t = time.strptime(row[j+2],'%H:%M:%S')
							s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
							avg_list[j] += s
						elif j == 13: 
							avg_list[j] = 0
						else:
							if j == 12:
								avg_list[j] += float(row[j+3])
							else:
								avg_list[j] += float(row[j+2])
						
		for k in range(col):
			avg_list[k] /= number
		avg_list[1] = avg_list[0] / avg_list[2]
		avg_list[13] = avg_list[12] / avg_list[9]
		print p+" : "
		for l in range(col):
			if l == 11:
				seconds = avg_list[l]
				minutes = seconds // 60
				print "%02d:%02d" % (minutes, seconds % 60)
			else:
				print avg_list[l]


			

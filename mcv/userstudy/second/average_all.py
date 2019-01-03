import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4", "Problem 5"]
group = ["A", "B", "C"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","time","confidence"]

#number = 44
number = 29
col = 11
for p in prob:
	with open('combine_ba_bc.csv', 'rb')as csvfile:
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
						if j != 9: avg_list[j] += float(row[j+3])	
						else:
							t = time.strptime(row[j+3],'%H:%M:%S')
							s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
							avg_list[j] += s
						
		for k in range(col):
			avg_list[k] /= number
		print p+" : "
	
		for l in range(col):
			if l == 9:
				seconds = avg_list[l]
				minutes = seconds // 60
				print "%02d:%02d" % (minutes, seconds % 60)
			else:
				print avg_list[l]

		speru = avg_list[9] / avg_list[1]		
		mperu = speru // 60
		print "%02d:%02d" % (mperu, speru % 60)

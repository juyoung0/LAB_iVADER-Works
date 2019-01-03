import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4", "Problem 5"]
group = ["A", "B", "C"]
col = ["problem","group","user","time"]

#number = 49
#number = 88
#number = 103
#number = 15
#number = 97
number = 44
col = 4
for p in prob:
	with open('before_modify_time.csv', 'rb')as csvfile:
        	firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		avg_time = 0.0
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if p == row[0]:
					for j in range(col):	
						if j == 3:		
							t = time.strptime(row[j],'%H:%M:%S')
							s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
							avg_time += s
						

		avg_time /= number
		print p+" : "
		seconds = avg_time
		minutes = seconds // 60
		print "%02d:%02d" % (minutes, seconds % 60)

			

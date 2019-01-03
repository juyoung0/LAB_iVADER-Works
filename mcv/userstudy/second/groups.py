import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4", "Problem 5"]
#group = ["A", "B", "C", "D", "E"]
#group = ["A", "B", "C", "D"]
group = ["A", "B", "C"]
col = ["problem","group","user","time"]

groupN = 3
col = 4

for p in prob:
	with open('before_modify_time.csv', 'rb')as csvfile:
       		firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		avg_time = [None]*groupN
		group_num = [None]*groupN
		for n in range(groupN):
			group_num[n] = 0
			avg_time[n] = 0.0	
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if True :
					if p == row[0]:
        	        	                g = ord(row[1])-65
                        		        group_num[g] += 1
						
                	                        t = time.strptime(row[3],'%H:%M:%S')
                        	                s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
	                                        avg_time[g] += s
		for m in range(groupN):
			avg_time[m] /= group_num[m]

		for i in range(groupN):
			print "Group "+chr(i+65) + " : " +str(group_num[i])
		
                    	seconds = avg_time[i]
                        minutes = seconds // 60
                       	print "%02d:%02d" % (minutes, seconds % 60)
	

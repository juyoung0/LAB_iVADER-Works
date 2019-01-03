import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4"]
group = ["A", "B", "C", "D"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time","sess","confidence"]
a = 
ba = ["S5", "S6", "S27", "S29", "S31", "S37", "B12", "B26", "B28", "B29", "B37", "B39", "B43", "B44", "B46"]

number = 29 #a
#number = 68 #b
#number = 15 #ba
#numver = 53 #bc

for p in prob:
	with open('withoutD.csv', 'rb')as csvfile:
        	firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		avg_list = [None] * 12
		for i in range(12):
			avg_list[i] = 0.0
		
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if p == row[0]:
					for j in range(12):
						if j == 10:
							t = time.strptime(row[j+3],'%H:%M:%S')
							s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
							avg_list[j] += s
						else:
							if j == 11:
								avg_list[j] += float(row[j+4])
							else:
								avg_list[j] += float(row[j+3])
						
		for k in range(12):
			avg_list[k] /= number
		print p+" : "
		for l in range(12):
			if l == 10:
				seconds = avg_list[l]
				minutes = seconds // 60
				print "%02d:%02d" % (minutes, seconds % 60)
			else:
				print avg_list[l]


			

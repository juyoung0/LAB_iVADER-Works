import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4"]
group = ["A", "B", "C"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time","sess","confidence"]
ba = ["S5", "S6", "S27", "S29", "S31", "S37", "B12", "B26", "B28", "B29", "B37", "B39", "B43", "B44", "B46"]
bc = ["S3","S4","S7","S8","S9","S10","S12","S16","S18","S19","S20","S21","S22","S23","S24","S25","S26","S28","S30","S32","S33","S34","S36","A1","A6","A9","A11","A12","A21","B4","B13","B14","B15","B16","B17","B18","B19","B20","B21","B22","B24","B27","B31","B32","B33","B34","B35","B36","B40","B42","B45","B48","B49"]


#number = 29 #a
#number = 68 #b
#number = 15 #ba
number = 53 #bc

col = 11
with open('withoutD.csv', 'rb')as csvfile:
       	firstrow = True
	spamreader = csv.reader(csvfile, delimiter=',')
	avg_list = [None] * col
	tot_list = [None] * col
	for i in range(col):
		avg_list[i] = 0.0
		tot_list[i] = 0.0
	
	for row in spamreader:
		if firstrow:
			firstrow = False
		else:
			if row[2] in bc:
				print row[2]
				if row[0] != "Problem 5":
					for j in range(col):
						if j == 10:
							t = time.strptime(row[j+3],'%H:%M:%S')
							s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
							avg_list[j] += s
						else:
							avg_list[j] += float(row[j+3])
	
				if row[0] == "Problem 4":	
						
					for j in range(col):
						tot_list[j] += avg_list[j]

					for j in range(col):
						avg_list[j] = 0.0
	for i in range(col):
		tot_list[i] /= number
		tot_list[i] /= 4
		print tot_list[i]

	s = tot_list[10]
	m = s // 60
	tot_list[10] = "%02d:%02d" % (m, s%60)
	print tot_list

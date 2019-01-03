import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4"]
group = ["A", "B", "C"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time","sess","confidence"]
ba = ["S5", "S6", "S27", "S29", "S31", "S37", "B12", "B26", "B28", "B29", "B37", "B39", "B43", "B44", "B46"]

#number = 29 #a
#number = 68 #b
number = 15 #ba
#numver = 53 #bc

col = 11
with open('withoutD.csv', 'rb')as csvfile:
	with open('bc.csv', 'wb')as wfile:
        	firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		spamwriter = csv.writer(wfile, delimiter=',')
		spamwriter.writerow(['Group','User','Time','View','Accuracy', 'Annotation'])
		avg_list = [None] * col
		tot_list = [None] * col
		for i in range(col):
			avg_list[i] = 0.0
			tot_list[i] = 0.0
	
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if row[2] in ba:
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
						s = avg_list[10] / 4
						v = avg_list[1] / 4
						a = avg_list[8] / 4
						an = avg_list[2] / 4
						m = s // 60
						t = "%02d:%02d" % (m, s%60)
						spamwriter.writerow([row[1], row[2], s, v, a, an])

						for j in range(col):
							avg_list[j] = 0.0
#						for j in range(col):
#							tot_list[j] += avg_list[]

#		for i in range(col):
#			tot_list[i] /= number


		print avg_list

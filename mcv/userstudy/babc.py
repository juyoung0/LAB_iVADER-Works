import csv
import datetime
import time
prob = ["Problem 1", "Problem 2", "Problem 3", "Problem 4"]
group = ["A", "B", "C"]
col = ["problem","group","user","logs","units","annotation","unit branch","session branch","Parallel Coordinate Plot","Scatter Plot","Scatterplot Matrix","Accuracy","restore","time","sess","confidence"]

number = 44
col = 11
with open('withoutD.csv', 'rb')as csvfile:
	with open('babc.csv', 'wb')as wfile:
        	firstrow = True
		spamreader = csv.reader(csvfile, delimiter=',')
		spamwriter = csv.writer(wfile, delimiter=',')
		spamwriter.writerow(['Group','User','Time','View','Annotation'])
		a_avg_list = [None] * col
		b_avg_list = [None] * col
		a_num = 0
		b_num = 0
		for i in range(col):
			a_avg_list[i] = 0.0
			b_avg_list[i] = 0.0
	
		for row in spamreader:
			if firstrow:
				firstrow = False
			else:
				if row[0] != "Problem 5":
					if row[1] == "E":
						a_num += 1
					elif row[1] == "B":
						b_num += 1

					for j in range(col):
						if j == 10:
							t = time.strptime(row[j+3],'%H:%M:%S')
							s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
							if row[1] == "E":
								a_avg_list[j] += s
							elif row[1] == "B":
								b_avg_list[j] += s
						else:
							if row[1] == "E":
								a_avg_list[j] += float(row[j+3])
							elif row[1] == "B":
                                                                b_avg_list[j] += float(row[j+3])

				if row[0] == "Problem 4":
					if a_num != 0 :
						s = a_avg_list[10] / a_num
						v = a_avg_list[1] / a_num
						a = a_avg_list[2] / a_num
						m = s // 60
						t = "%02d:%02d" % (m, s%60)
						spamwriter.writerow(["A", row[2], s, v, a])
                                        if b_num != 0 :
                                                s = b_avg_list[10] / b_num
                                                v = b_avg_list[1] / b_num
                                                a = b_avg_list[2] / b_num
                                                m = s // 60
                                                t = "%02d:%02d" % (m, s%60)
						spamwriter.writerow(["B", row[2], s, v, a])

					for i in range(col):
						a_avg_list[i] = 0.0			
						b_avg_list[i] = 0.0

					a_num = 0
					b_num = 0
						


		

import csv

with open('time.csv', 'rb')as csvfile:
       	firstrow = True
	spamreader = csv.reader(csvfile, delimiter=',')
	avg_list = [None] * 10
	
	for row in spamreader:
		if firstrow:
			firstrow = False
		else:
		
			for k in range(6):
				if k!= 0:
					print row[k]			


				

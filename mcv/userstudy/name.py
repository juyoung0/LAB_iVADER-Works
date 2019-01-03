import csv

names = []
with open('car.csv', 'rb')as csvfile:
        firstrow = True
	spamreader = csv.reader(csvfile, delimiter=',')
		
	for row in spamreader:
		if firstrow:
			firstrow = False
		else:
			names.append(row[0])	

	print names

				

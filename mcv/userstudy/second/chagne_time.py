import csv
import datetime
import time

with open('time.csv', 'rb')as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		t = time.strptime(row[0],'%H:%M:%S')
		s = datetime.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
		print s
#		m = s // 60
#		print "%02d:%02d" % (m, s % 60)

			

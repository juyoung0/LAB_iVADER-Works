import csv

r = csv.reader(open('tag_threshold.csv'))
lines = list(r)

for i in range(237):
	newtag = "KEWP_35"+lines[i][0].replace(" ","_")
	lines[i][0] = newtag

writer = csv.writer(open('tag_threshold_md.csv','w'))
writer.writerows(lines)

import csv
import codecs

name = ["ojy/OJY_", "ksy/KSY_", "kyj/KYJ_", "shk/SHK_"]
test = ["none", "normal", "random"]

for i in range(4):
	for j in range(3): 

		with open(name[i]+test[j]+".txt","rb") as infile, open("result/"+name[i]+test[j]+".csv","wb") as outfile:
			in_txt = csv.reader((line.replace('\0','') for line in infile))
			out_csv = csv.writer(outfile)
			out_csv.writerow(["time","angle"])
			out_csv.writerows(in_txt)

import csv
import codecs

name = ["kja/kja_r2l_","kja/kja2_r2l_","kja/kja_l2r_","kja/kja2_l2r_"];
test = ["random"]

for i in range(4):
	for j in range(1): 

		with open(name[i]+test[j]+".txt","rb") as infile, open("result/"+name[i]+test[j]+".csv","wb") as outfile:
			in_txt = csv.reader((line.replace('\0','') for line in infile))
			out_csv = csv.writer(outfile)
			out_csv.writerow(["time","angle"])
			out_csv.writerows(in_txt)

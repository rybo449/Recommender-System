import sys
import csv
f = open(sys.argv[1])
reader = csv.reader(f)

for i in reader:
	print "\""+i[0]+"\""+",",
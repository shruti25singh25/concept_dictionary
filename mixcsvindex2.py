import operator
import re
import os
import numpy as np
f1=open('result.txt','r')
#f1=open('developerindex3','r')
#f2=open('sorting.out','w')
lines = f1.readlines()
GlobalList = []

for line in lines:
        line = line.split()
	GlobalList.append(line)

line2 = GlobalList
line3 = sorted(line2, key=operator.itemgetter(0))
#print line3


for i in range(len(line3)):
	#print line3[i]

	myString = " ".join(line3[i])
	print myString



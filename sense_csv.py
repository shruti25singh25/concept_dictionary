#Author: Shruti Singh, M.Tech(CS), Banasthali University

import os
import glob
import csv
my_dir = "/home/shruti/create-hindi-parser/chl_to_dmrs/sense_modified_csv"
f = open('sense_data.out','a')
#f = open('srr2','a')
f.write('\n+++++++++++sense_modified_data++++++++++')
filelist = []
os.chdir( my_dir )
for files in glob.glob( "*.csv" ):
        filelist.append(files)

#f.write( filelist[files])

for line in filelist:
        reader = csv.reader( open( line, 'rb'), )
        lines = list(reader)
        l= lines[:100]
        lengtheng = len(l[0])
        lengthhin = len(l[1])
        lengthpos = len(l[3])
        lfirst = l[0]


        Diff_Eng_Hin = lengtheng - lengthhin
        if Diff_Eng_Hin == 1 :
                l[1].append('X')
        if Diff_Eng_Hin == 2 :
                l[1].append('X')

        Diff_Eng_Pos = lengtheng - lengthhin
        if Diff_Eng_Hin == 1 :
                l[3].append('X')
        if Diff_Eng_Hin == 2 :
                l[3].append('X')
                l[3].append('X')


        for x in range(0,lengtheng):
                first = l[0][x]
                first = first.split('_')
#               first = first.split('-')
                first = first[0]
                first = first.split('-')
                first1 = first[0]
#               print "*****",first
                f.write('\n' +first1)
                f.write(',')
                f.write(l[3][x])
                f.write(',')
                f.write(l[1][x])


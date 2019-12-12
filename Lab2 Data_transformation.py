# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:17:14 2019

@author: vikash
"""
import pandas as pd
import itertools
import numpy as np
import statistics
filename = 'Data Set\IPL\matches.csv'
result= pd.read_csv(filename)

#Z score Transformation
# prepare data for normalization

saved_column = input("Enter Column Name : ")
saved_column=result[saved_column]
id1=0
#row_no= 5
row_no= int(input("Enter row_no : "))
for row in itertools.islice(saved_column,0,row_no):
    print(id1,'',row)
    id1+=1;
#array=np.array(saved_column)
#print(array)


minA = min(i for i in saved_column if i is not 0)
maxA = max(saved_column)

maxN=1
minN=0
avg=statistics.mean(saved_column)
sd=statistics.stdev(saved_column)
## Z value for each data

print('The Z values for every data are:')
for x in saved_column:
    a1=(x - avg)/sd
print(round(a1,2))

print('The Min-Max values for every data are:')
for x in saved_column:
    #a1=[[x - np.min(array)]/np.max(array)-np.min(array)]
    a1=((x-minA)/(maxA-minA))*(maxN-minN)+minN
print(round(a1,2))

print('The normalization and decimal:')
for x in saved_column:
    a1=(x/100)
print(a1)


print()
print('The minimum run is:',minA)
print('The maximum run is:',maxA)
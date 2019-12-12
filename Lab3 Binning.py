# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:36:06 2019

@author: vikash
"""

import pandas as pd
import array
import statistics
import numpy as np
filename = 'Data Set\IPL\matches.csv'
result= pd.read_csv(filename)
#print(result)
print("\n\nThe proceesing is performed to find average run win and win by min/max run won by team bowling second\n\n")
saved_column = input("Enter Column Name : ")
saved_column=result[saved_column]
#saved_column=result[saved_column]
#print(saved_column.count)
array=np.array(saved_column)
print("\n\nBeffore sorting\n\n\n",array)
bin_1 = []
array1=np.sort(array)
print("\nSorted Array\n\n",array1)



#row_no= 5

bin1=saved_column[0:211]  
bin2=array1[212:423]
bin3=array1[422:636] 

mean1=bin1.mean()
mean2=bin2.mean()
mean3=bin3.mean()
print("\nBin by Mean")
print("First bin",round(mean1,2))
print("Second bin",round(mean2,2))
print("Third bin",round(mean3,2))

max1=bin1.max()
max2=bin2.max()
max3=bin3.max()
#minA = min(i for i in saved_column if i is not 0)
min1=bin1.min()
min2=bin2.min()
min3=bin3.min()
print("\nBin by Min-Max(Boundaries)")
print("First bin",min1,max1)
print("Second bin",min2,max2)
print("Third bin",min3,max3)



print(bin1.values.reshape(211))
print(bin2)
print(bin3)
'''
print("[",bin1,"]","[",bin1,"]","[",bin1,"]",)
'''

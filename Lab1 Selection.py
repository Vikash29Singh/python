# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:28:08 2019

@author: vikash
"""

"""
Selecting best column on the basis of team winning toss,toss_decision,reult,winner etc.
worst case which is not necessary for analyze purpose
"""
import pandas as pd
import numpy as np
#import random
print ("BY USING THE DATA SET:")
print ("**********************")
#1: read dataset into pandas from data frames
filename = 'Data Set\IPL\matches.csv'
result= pd.read_csv(filename)
#2 : read n create list of all features
list_all = list(result.columns.values)
print("LIST:",list_all)
#3 : define best features list
random_best_list = [4,5,6,7,8,10,11,12]
#random_best_list.sort()
#data_top = result.head() 
best_columns = list(result.columns[random_best_list])
#print(random_best_list.head())
print("BEST:",best_columns)
#To print top 10 datas
res=result[best_columns]
print(res.loc[[i for i in range(10)]])
#data_top
#4 : define worst features list
worst_columns = [i for i in list_all if i not in best_columns]
print("WORST:",worst_columns)
#To print top 10 datas
res1=result[worst_columns]
print(res1.loc[[i for i in range(10)]])






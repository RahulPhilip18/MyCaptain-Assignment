# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:17:07 2022

@author: rahul
"""

str=input('Enter a string: ')
print('String is',str)
count={}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1
print(count)

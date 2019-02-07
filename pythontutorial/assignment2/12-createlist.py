# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:41:32 2018

@author: Raghu Prasad
"""

#[4,5,6]

mylist = []
for ele in range(4,7):
    print(ele)
    mylist.append(ele)
print(mylist)

#[-2,1,3] -2,-1,0,1,2,3


mylist1 = []
slice1 =[]
for ele in range(-2,5):
    print(ele)
    mylist1.append(ele)
    slice1 = mylist1[::3]
    slice1[len(slice1)-1] = slice1[len(slice1)-1]-1
print(slice1)




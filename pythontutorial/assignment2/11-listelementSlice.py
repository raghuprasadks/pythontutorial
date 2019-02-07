# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:16:49 2018

@author: Raghu Prasad
"""
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
slc1 = lst[5:15:2]
print('slc 1 ' ,slc1)
slc2 = lst[::4]
print('slc 2 ',slc2)
sum=avg=0

for a in slc1:
    sum+= a
    print(a,end=' ')
print()
print("Sum of elements of slice 1 :",sum)

print("Slice 2")
sum=0
for a in slc2:
    sum+=a
    print(a,end=' ')
print()
avg=sum/len(slc2)
print("Average of elements of slice 2 ",avg)

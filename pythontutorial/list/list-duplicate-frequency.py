# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 19:31:32 2018

@author: Raghu Prasad
"""
# Program to find frequencies of all the elements of a list.
# Also,print the list of unique elements in the list
# and duplicate elements in the given list
lst = eval(input ("enter list"))
length = len(lst)
unique = []
duplicate = []
counter = 0
i = 0
while i <length:
    element = lst[i]
    count = 1
    if element not in unique and element not in duplicate:
        i += 1
        for j in range (i,length):
            if element == lst[j]:
                count +=1
        else:
            print("Element ",element,"frequency", count)
            if (count ==1):
                unique.append(element)
            else:
                duplicate.append(element)
    else:
        i += 1
print("original list ",lst)
print("Unique list ",unique)
print("duplicate list ",duplicate)


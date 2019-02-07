# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:15:17 2018

@author: Raghu Prasad
"""
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Access Items
for x in thisset:
  print(x)

#Check if "banana" is present in the set:
print("banana" in thisset)
#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#add
print(thisset)
#update
thisset.update(["orange", "mango", "grapes"])
print(thisset)
#length
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#remove
thisset.remove("banana1")
print(thisset)
#Note: If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana1")
print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#pop
x = thisset.pop()
#Clear empties the set
thisset.clear()
#del deletes the set completely
del thisset
# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
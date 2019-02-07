import keyword as k
print(k.kwlist)

#import keyword
#iskeyword('str')

#command line arguments

import sys
print ("number of arguments",len(sys.argv))
print ("argument lists",str(sys.argv))
print ("argument lists %s",%(sys.argv[1]))

#python commonad_line.py 'hello' 'world'
#2.7 both raw_input and input
#raw input converts every thing to string
name = input("What is your name")
age = input("What is your age")
#3.0 functionality of raw__input is renamed as input. hence automatic conversion
#is not happening
print('name',name)
print('name',age)
print('type age',type(age))
print('type name',type(name))

#no do-while in python

#for loop
#for {variable} in {sequence}


list=[1,2,3,4]
dir(list)
#should be a _iter_
for i in list
    print(i)

#for /while
 #   you can put else:
#after the end of the condition

list = ['learning','python']
for word in list:
    if 'python'==word:
        print("found")
        break
else:
    print("not found")

range(10) #0 to 9 default step 1
range(0,10,1) #start,end and step

for i in range(10):
    print(i)

#range(stop)
#range(start,stop)
#range(start,stop,increment)

#map

from operator import add
list1=[1,2,3]
list2=[4,5,6]
map(add,list1,list2)

#zip
list3=[]
for i in zip(list1,list2):
    print(sum(i))
    list3.append(sum(i))

#list comprehension

list3=[sum(i) for i in zip(list1,list2)]
print list3

#tuple
tup = tuple(range(5))
print dir(tup)

any or all

tup = ('python','java''scala')
new_tup=zip(range(3),tup)

enumerate(tup)
tuple(enumerate(tup))

#generator lazy valuation

#set
list1=[1,1,2,3,2]
list2=[1,3,4,6]
set(list1)|set(list2)
&
-

import os
os.getcwd()
import subproces
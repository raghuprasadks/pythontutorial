#In Python, anonymous function is a function that is defined 
#without a name.
#While normal functions are defined using the
# def keyword, in Python anonymous functions are defined 
# using the lambda keyword.
#Hence, anonymous functions are
# also called lambda functions.
#syntax
# lambda arguments: expression
#Lambda functions can have any number of arguments but 
#only one expression. The expression is evaluated and returned. 
#Lambda functions can be used wherever function objects are 
#required.
#Even numbers

def double(x):
    return x *2
double(10)

double = lambda x: x * 2
# Output: 10
print(double(5))
#Filter
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# Output: [4, 6, 8, 12]
print(new_list)
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)

#Python Program To Display Powers of 2 Using 
#Anonymous Function
# Change this value for a different result

terms = int(input("How many terms? "))
for i in range(terms):
    print(i)
# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
#print("Result",result)
# display the result
#print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
#Output
'''
The total terms is: 10
2 raised to power 0 is 1
2 raised to power 1 is 2
2 raised to power 2 is 4
2 raised to power 3 is 8
'''

#Python Program to Find Numbers Divisible by Another Number
# Python Program to find numbers divisible by thirteen 
#from a list using anonymous function
# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221]
# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))
# display the result
print("Numbers divisible by 13 are",result)
# Python code to illustrate  
# reduce() with lambda() 
# to get sum of a list 
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 

#Here the results of previous two elements are added to the next element 
#and this goes on till the end of the list like (((((5+8)+10)+20)+50)+100).

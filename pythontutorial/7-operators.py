#Arithmetic Operators

#Addition
x= 4
y= 5
print(x + y)

#Subtraction
x= 4
y= 5
print(x - y)

#Multiplication
x= 4
y= 5
print(x * y)

#Division
x= 8
y= 4
print(x / y)

#Modulus
x= 8
y= 4
print(x % y)

#Exponent
x= 2
y= 3
print(x**y)

#comparion
x = 4
y = 5
print('x > y  is',x>y)

#Assignment
num1 = 4
num2 = 5
print ("Line 1 - Value of num1 : ", num1)
print ("Line 2 - Value of num2 : ", num2)

#compound assignment
num1 = 4
num2 = 5
res = num1 + num2
#res = res +num1
res += num1
#res = res -num1
res -= num1
print ("Line 1 - Result of + is ", res)
#Logical Operators
a = True
b = False
print('a and b is',a and b)
print('a or b is',a or b)
print('not a is',not a)

#Membership
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")

if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")

#Identity Operators
x = 30
y = 30

if (x is y):
    print("x & y  SAME identity")
else:
    print ("x and y are not having same identify")
y = 30
if (x is not y):
    print("x & y have DIFFERENT identity")
#Operator precedence
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
# 4 + 5 = 9
#9*8/2
#72/2
#36
print("Value of (v+w) * x/ y is ",  z)

# single line comment

"""
this is multi line comment
this is second line
"""

'''
this is my comment first line
this is my second line
'''
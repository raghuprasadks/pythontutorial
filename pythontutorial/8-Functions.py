#Function
def func1():
    print('I am learning python  function')
    
func1()
#Square
def square(x):
    y = x*x
    print('Square of : ',x,'is ', y)
square (3)
#Square with return value
def square(x):
    y=x*x
    return y
z=square(4)
print('Square:Return Value', z)
print('Square of 5:Return Value ', square(5))
#Function Arguments
def multiply(num1,num2):
    print(' num1 :', num1, ' num2 :', num2)
    return num1*num2
product = multiply(10,12)
print('product : ',product)
product = multiply(num2=10,num1=15)
print('product : ',product)

#Function with multiple arguments
def multiple(*args):
    print(args)

multiple(1,3,4,5,7,9,10)
multiple(4,5)


# Write a function to calculate simple interest

# i = prt/100

# Write a function to convert from fahrenheit to celcius

#Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
#Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C
def simpleInterest(p,r,t):
    i = (p*r*t)/100;
    return i;
interest = simpleInterest(1000,6,1)
print('Simple interest is ',interest)
p = float(input('Enter principal amount'))
r = float(input('Enter Rate of interest'))
t = float(input('Enter Time in year'))
interest = simpleInterest(p,r,t)
print('Simple interest is ',interest)




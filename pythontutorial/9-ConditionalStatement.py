print(__name__)
#IF
def main():
    x,y=2,8
    if(y>x):
        print ('Y is Greater ',y)      
#main()
if(__name__=="__main__"):
    main()
#Else
def main():
    x,y=10,8
    if(y>x):
        print ('Y is Greater ',y)
    else:
        print('X is Greater ', x)
if(__name__=="__main__"):
    main()
#Else both number is same

def main():
    x,y=10,10
    if(y>x):
        print ('Y is Greater ',y)
    else:
        print('X is Greater ', x)
if(__name__=="__main__"):
    main()

#elif
def main(country,total):
    #total = 100
    #country = "US"
    #country = "AU"
    if country == "US":
        if total <= 50:
            print("Shipping Cost is  $30")
        elif total <= 100:
            print("Shipping Cost is $25")
        elif total <= 150:
            print("Shipping Costs $5")
    elif country == "AU":
        if total <= 50:
                print("Shipping Cost is  $100")
        else:
            print("FREE")
    else:
        print("Our service is not available")
    if(__name__=="__main__"):
        country = input("Enter country")
        amtpurchased = int(input("Enter amout purchased"))
        main(country,amtpurchased)
    

# Simple calculator
    
 ''' 
 Program make a simple calculator that can
 add, subtract, multiply and divide using 
 functions '''

# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user 
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
   
#Specify a Variable Type

#int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)   
#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
#Integer
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#String
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


# usage of if

#age = 20
name = input("Enter your name")
age = int(input("Enter your age"))

print('type of name ',type(name))
print('type of age ',type(age))

if(age>=18):
    print(name ,' You are eligible to vote')
elif(age<18):
    print(name ,'you are not eligible to vote')
else:
    print('invalid age')
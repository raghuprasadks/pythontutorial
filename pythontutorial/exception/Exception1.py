#with out expection handling
n = int(input('Enter a number to validate division by zero'))

div = 100/n

print('result is ',div)


d = int(input('Enter a number to validate division by zero'))
try:
    a=10/d
    print(a)
except ArithmeticError:
    print("This statement is raising an exception")
else:
    print("No exception proceed")

#Except with no exception

try:
    a=10/0
    print(a)
except:
    print("Exception")
else:
    print("Proceed no exception")

#Declaring multiple exception

try:
    a=10/0
    #a=10/'raghu'
    print(a)
#except ArithmeticError,NameError: - 3.6 does not support
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ZeroDivisionError")
except:
    print("Generic Error")
else:
    print("Successfully Done")
#Finally Block

try:
    #a=10/0;
    a=10/2;
    print(a)
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("Finally block is always called")

#Raise an exception

try:
    a=10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occured")
    print(e)

#Custom exception

class ErrorInCode(Exception):
    def __init__(self,data):
     self.data = data
    def __str__(self):
        return repr('Error Code ' +str(self.data))
try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
#except ErrorInCode:
    print("Received error :",ErrorInCode)
    print("Received error :",ae)

class Student(object):
	def __init__(self, name, age, twitter_url=None, google_plus=None, youtube_channel=None):
		self.name = name
		self.age = age
		self.twitter_url = twitter_url
		self.google_plus = google_plus
        self.

	def __str__(self):
		# Override to print a readable string presentation of your object
		# below is a dynamic way of doing this without explicity constructing the string manually
		return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

student = Student(name='Jone', age=23, twitter_url='http://twitter.com/jone')
print(student)
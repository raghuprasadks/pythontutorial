# https://www.python-course.eu/python3_object_oriented_programming.php

class Robot:
    pass

if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y == x)

class Robot:
    pass

x = Robot()
y = Robot()
 
x.name = "Marvin"
x.build_year = "1979"

y.name = "Caliban"
y.build_year = "1993"
 
print(x.name)
print(y.build_year)

print(x.__dict__)
print(y.__dict__)


def hi(obj):
    print("Hi, I am " + obj.name + "!")

class Robot:
    pass
    

x = Robot()
x.name = "Marvin"
hi(x)


def hi(obj):
        print("Hi, I am " + obj.name)

class Robot:
    say_hi = hi
    

x = Robot()
x.name = "Marvin"
Robot.say_hi(x)

class Robot:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name + "', " +  str(self.build_year) +  ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " +  str(self.build_year)
     
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
        
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    new = eval(x_str)
    print(new)
    print("Type of new:", type(new))
    
    
'''
name	Public
These attributes can be freely used inside or outside of a class definition.
_name	Protected
Protected attributes should not be used outside of the class definition, unless inside of a subclass definition. 
__name	Private
This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.
 '''
  
class A():
    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

#from attribute_tests import A
x = A()
print('public ',x.pub)
x.pub = x.pub + " and my value can be changed"
print('public value is changed', x.pub)
print('protected ',x._prot)
print('private ', x.__priv)

class Robot:
 
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
        
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
            
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name    

    def set_build_year(self, by):
        self.__build_year = by
        
    def get_build_year(self):
        return self.__build_year    
    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)

     
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")
        

class A():
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def GetX(self):
        return self.__x

    def GetY(self):
        return self.__y

    def SetX(self, x):
        self.__x = x

    def SetY(self, y):
        self.__y = y
        
class Robot():
    
    def __init__(self, name):
        print(name + " has been created!")
        
    def __del__(self):
        print ("Robot has been destroyed")
        
        
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y

class Robot():
    
    def __init__(self, name):
        print(name + " has been created!")
        
    def __del__(self):
        print (self.name + " says bye-bye!")
        
        
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y

#Setters and Getters
class P:

    def __init__(self,x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x
        
p1 = P(42)
p2 = P(4711)
print('x ',p1.x)
p1.x = 47
p1.x = p1.x + p2.x
print(p1.x)


 
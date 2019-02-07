class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print('Barking')
d= Dog()
d.eat()
d.bark()
#Multi level
class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print('Barking')
class BabyDog(Dog):
    def weep(self):
        print('Weeping ')
d= BabyDog()
d.eat()
d.bark()
d.weep()


# Constuctor

class Car():
    def __init__(self,model,make,yom,price):
        print('constructor')
        self.model = model
        self.make = make
        self.yom = yom
        self.price = price
    def __del__(self):
        print('destructor')
myFirstCar = Car('Aasta','Hyundai',2014,65000)
mySecondCar = Car('800','Maruti',2007,25000)
del mySecondCar

# Multiple Inheritance
class Parent(object):
    def __init__(self):
        #super(Parent,self).__init__()
        print("Parent")
class Child():
    def __init__(self):
       # super(Child,self).__init__()
        print("Child")
class GrandChild(Child,Parent):
 '''   def __init__(self):
     #   super(GrandChild,self).__init__()
        print("GrandChild")
'''
GrandChild()

#Method overloading
class Human:
    def sayHello(self, name=None,city=None):
        if name is not None and city is not None:
            print('Name is ' , name ,' and city is ',city)
        elif city is not None:
            print('City is ' + city)
        elif name is not None:
            print('Name is ' + name)
        else:
            print('Hello ')   
# Create instance
obj = Human()
# Call the method
obj.sayHello()
# Call the method with a parameter
obj.sayHello('To Python')
obj.sayHello(city='Bengaluru')
obj.sayHello('To Java','Bengaluru')
# Method Overriding
class Base(): # Base class
    def add(self,a,b):
        s=a+b
        print ('Add in Base class :',s)
        print(s)

class Derived(Base): # Derived class
#    pass
    def add(self,a,b): # overriding method
        sum=a+b+3
        print('Add in derived class :',sum)
    def future():
        pass

base_inst=Base() #instance creation for Base class
deri_inst=Derived()#instance creation for Derived class
base_inst.add(4,3) # function with 2 arguments
deri_inst.add(4.0,8.5)   # function with 2 arguments


# Class with pass

class PassClass():
    pass

justPass = PassClass()
justPass.dummyparam1 = 'Dummy 1'
justPass.dummyparam2 = 'Dummy 2'
print('Dummy Variables', justPass.dummyparam1,justPass.dummyparam2)

# public,private and protected

class Student():
    def __init__(self,name,age,mobile):
        #public variable name
        self.name = name
        #private varaible
        #self.__age=age
        self.age=age
        #protected varaible
        self._mobile=mobile
        
    def info(self):
        print ('My info : Name :',self.name, '  Age :',self.age, ' Mobile :',self.mobile)
        
ravi = Student('Ravi Kumar',21,9845547471)
ravi.info()
print('name ',ravi.name)
print('mobile ',ravi.mobile)
class MyClass:
    "This is python MyClass"
    a=50
    def func(self):
        print("Welcome to python")
print (MyClass.a)
print(MyClass.__doc__)

ob = MyClass()
print(ob.__doc__)
print(ob.a)
ob.func()

#Student Class

class Student:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
    def displayStudent(self):
        print("Roll No : ",self.rollno, " Name : ",self.name)

stud1 = Student(100,"Raghu")
stud2 = Student(101,"Rakesh")
stud1.displayStudent()
stud2.displayStudent()

class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real = r
        self.imag = i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

c1=ComplexNumber(5,6)
c1.getData()
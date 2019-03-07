#Class
class myClass():    
    def method1(self):
        print("myClass:method1")
    def method2(self, name):
        print("myClass:method2:Name " , name)
def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2("Python")
    
    c1 = myClass()
    c1.method1()
    c1.method2("Machine Learning")
if (__name__ == "__main__"):
    main()

#Inheritance
class myClass():
    def method1(self):
        print("Parent:method1")
    def method2(self, name):
        print("Parent Method 2 :",name)
    def method3(self,city):
        print ("You are from ", city)
#class childClass():
class childClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("ChildClass:method1")
    def method2(self):
        print("childClass:method2")
def main():
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    c2.method2()
    c2.method3("Bengaluru")
if (__name__ == "__main__"):
    main()
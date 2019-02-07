# Multiple Inheritance
class First(object):
    def __init__(self):
        super(First,self).__init__()
        print("first")
class Second(object):
    secondclsattr ="second"
    def __init__(self):    	
        super(Second,self).__init__()
        print("second")
class Third(Second,First):
    def __init__(self):  	
#       super(Third,self).__init__()
        print("Third")
trd = Third()
print(trd.secondclsattr)
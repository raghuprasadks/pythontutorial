class C:
    "this is python class"
    a = 5
    b = [1,2,3]
    def foobar():
        b = "hi"    

#for attr, value in C.__dict__.iteritems():
for attr, value in C.__dict__.items():
    print ("Attribute: " + str(attr or ""))
    print ("Value: " + str(value or ""))
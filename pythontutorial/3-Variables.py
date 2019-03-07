#declare variable
a = 100
b = 'Bengaluru'
c = True
d = 150.5
print ('Variables a: ',a,' b: ',b,' c: ',c,' d: ',d)
print ('type ')
print (type(c))
#Reassinging values
a= 50
c= False
print ('Re-assigned : Variables a: ',a,' c: ',c)
#Concatenate
#print('kaushalya'+100)
a= 'kaushalya'
b = 100
#print(a+b)
print(a+' '+str(b))
print('printing ')
print(a,b,c)
print(b)
print(c)
print(' value of a is ',a,'\n value of b is ',b)
#Local and Global variables
p=100 # Global variable
print('Global scope:Initial ',p)
def localscope():
    #global p
    p=10
    print ('Local scope ',p)
    print ('Iam in this block')
print ('where am i')
localscope()
print ('Global Scope',p)

#Delete variable
f = 200
print("F :",f)

del f
print("F :",f)
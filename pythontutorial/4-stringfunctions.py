#Slicing index and range
var1 = 'kaushalya'
var2 = 'learning python'
print('0 th element of var1 : ',var1[0])
print('Slicing :',var2[0:8])
print(var2[:10])
print(var2[::2])
print(var2[::])
print('with offset 1')
print(var2[::1])
#length
print(len(var2))
#in - membership
print ("p" in var2)
print ("x" in var2)
#not in
print ("x" not in var2)
#Formatting -
name = 'guru'
number1 = 99
print("name is %s age is %d" %(name,number1))
#Concatenate
name = 'guru'
number = 99
print(name+str(number))
#Repeat
print (name*3)
#Replace
oldstring = 'I like python'
newstring = oldstring.replace('like','love')
print('Replace :',newstring)
oldstring = oldstring.replace('like','love')
print ('old string ',oldstring)
#Upper and Lower case
convertlower = 'This Is for LOWER'
print(newstring.upper())
print(convertlower.lower())
#capitalize
name = 'delhi is capital of india'
print('capitalize ', name.capitalize())
#Join
print(":".join("Python"))
print(",".join("Python"))
#Reverse
print('reverse ')
print(''.join(reversed(oldstring)))
#Split
word="Kaushalya Technical Training"
print(word.split(' '))
word="Kaushalya Technical Training"
print(word.split('a'))
#Immutable
x = "Kaushalya"
x.replace("Kaushalya","Python Training")
print(x)
#count
count1 = x.count('a',0,len(x))
print('count ',count1)


#built in list type

list1 =list()
print(list1)

#2ith range
list2 = range(5)
print(list2)

var ='python'
list3 = list(var)
print(list3)

#
language = ['c','java','python','c++','java script']
print('length ',len(language))

#index
print('index ',language[3])

#slicking
print('slicing ',language[1:3])

#negative

print('negative index ',language[-1])

#Append
language.append('scala')
print('Append ',language)

#Extend
language1 =['php','Lisp']
language.extend(language1)
print('Extend ',language)

#insert
language.insert(0,'JSP')
print('After insert ',language)

#index

print('index ',language.index("python"))
exists = "python" in language
print('Exists ',exists)

#Opeators +

print(language+['language 12','language 13'])

#+=
newlist = language += ["R"]
print('+= ',)

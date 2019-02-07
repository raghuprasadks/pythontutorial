#There are four collection data types in
# the Python programming language:

#List is a collection which is ordered 
#and changeable. Allows duplicate members.
#Tuple is a collection which is ordered 
#and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and 
#unindexed. No duplicate members.
#Dictionary is a collection which is 
#unordered, changeable and indexed. No duplicate members.
#List Mutable
data =[1,2,3,4]
print(data[0])
print(data[0:4])
print(data[-1])
print(data[-4:-1])
#Adding List
list1 = [10,20]
list2=[30,40]
list3=list1+list2
print(list3)
#Replicating lists
print(list1*2)
#List slicing
list1 = [1,2,3,4,5,6]
print(list1[0:3])
print(list1[3:6])
#Updating List
data1 = [5,10,15,20,25]
print("Original List ", data1)
data1[2] = "Fifteen"
print("After modification ",data1)
#Appending elements to the list
list1 = [10,20,30]
print('Before appending : ', list1)
list1.append(40)
list1.append([300,50])
print('After appending : ', list1)
#deleting
del list1[0]
del list1[0:2]
print('List after deleting ',list1)
#Functions and methods of lists
#Built in function
list1 = [2,9,3,56,23,89]
print('Minimum ',min(list1))
print('Maximum ',max(list1))
print('Length ',len(list1))
list3=[1,2,3]
list4=[5,6,7]
#list sequence
seq=(145,'abc','pqr')
data=list(seq)
print(' sequence ',data)
#Methods
#index
data=[3,5,6,7]
print('index of 6 ' ,data.index(6))
#count - occurance
data =[1,2,4,3,3,2,1,5,2]
print('count ',data.count(2))
#pop()/pop(int)
data = [786,'abc','a',123.5,786]
print ("Last element is", data.pop() )
print ("2nd position element:", data.pop(1) )
print (data)
#insert(index,object):
data=['abc',123,10.5,'a']
data.insert(2,'hello')
print (data)
#Extend
data1=['abc',123,10.5,'a']
data2=['ram',541]
data1.extend(data2)
print(data1)
print (data2)
#Remove
data1=['abc',123,10.5,'a','xyz','xyz']
data2=['ram',541]
print(data1)
data1.remove('xyz')
print(data1)
print (data2)
data2.remove('ram')
print (data2)
#Reverse
list1=[10,20,30,40,50]
list1.reverse()
print(list1)
#Sort
#list1=[10,50,13,'rahul','aakash']
list1=[10,50,13,2,46,6]
list1.sort()
print (list1)
list1.sort(reverse=True)
#Maximum element in a array
lst = eval(input ("Enter list :"))
length = len(lst)
print(" Length of list ", length)
sum = 0
mean = 0

for i in range (0,length):
	sum = sum +lst[i]
mean = sum/length
print("Given list is : ",lst)
print("Mean is  ",mean)

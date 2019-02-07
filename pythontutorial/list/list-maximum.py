#Maximum element in a array
lst = eval(input ("Enter list :"))
length = len(lst)
print(" Length of list ", length)
max_ele = lst[0]
max_index = 0
for i in range (1,length):
	if lst[i] > max_ele:
		max_ele = lst[i]
		max_index = i
print("Given list is : ",lst)
print("The maximum element of the given list is ",max_ele, " at index ",max_index)

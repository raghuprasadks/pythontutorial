#[100,40,20,50,2]
#Minimum element in a array
lst = eval(input ("Enter list :"))
length = len(lst)
print(" Length of list ", length)
min_ele = lst[0]
min_index = 0
for i in range (1,length):
	if lst[i] < min_ele:
		min_ele = lst[i]
		min_index = i
print("Given list is : ",lst)
print("The minimum element of the given list is ",min_ele, " at index ",min_index)

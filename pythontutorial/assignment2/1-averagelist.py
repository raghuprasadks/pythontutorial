# Find Sum,average,minimum and maximum of the entered numbers
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Sum and Average of elements in the list :",sum(a), round(avg,2))
print("Minimum ",min(a))
print("Maximum ", max(a))
#
num = int(input("enter the number"))
sum =0;
for i in range(1,num+1):
    sum = sum+i
avg = sum/num
print("sum is ",sum, "average is ",avg)
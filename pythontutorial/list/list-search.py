#Search an element in a array
lst = eval(input ("Enter list :"))
length = len(lst)
element = int(input(" Enter an element to be searched "))

for i in range (0,length):
    if element == lst[i]:
        print(element, " found ")
        break
else:
    print(element, " not found ")


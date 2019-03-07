# -*- coding: utf-8 -*-
class Customer():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
    	print('Name :',self.name,' Age : ',self.age)   
customers = []
# Single customer
print('Enter Customer Information')
name = input('customer name')
age =int(input('customer age'))
print('name :' ,name, ' age ',age)
customer1 = Customer(name,age)
customers.append(customer1)

# Multiple customer

print('Enter Customer Information')
noOfCustomers = int(input('No of Customers'))

for i in range(noOfCustomers):
    name = input('customer name')
    age =int(input('customer age'))
    print('name :' ,name, ' age ',age)
#customer1 = Customer(name,age)
    customers.append(Customer(name,age))

for c in customers:
    #print('name ',  customers[i].name)
    #print('age ',  customers[i].age)
    print('name check ',  c.name)
    print('age check ',  c.age)
    print('Customer info',c.display())
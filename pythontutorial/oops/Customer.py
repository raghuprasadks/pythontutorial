# -*- coding: utf-8 -*-
class Customer():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
    	print('Name :',self.name,' Age : ',self.age)
    
customers = []

customer1 = Customer('raghu',40)
customers.append(customer1)
customer2 = Customer('rakesh',22)
customers.append(customer2)
print('Customers :name ',customers[0].name)
print('Customers :age ',customers[0].age)
print('Customer info',customer[0].display())
#for i,c in enumerate(customers):
for c in customers:
    #print('name ',  customers[i].name)
    #print('age ',  customers[i].age)
    print('name check ',  c.name)
    print('age check ',  c.age)
    print('Customer info',c.display())
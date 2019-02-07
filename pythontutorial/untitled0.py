# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:04:07 2019

@author: Raghu Prasad
"""

class product(object):
    def __init__(self,no,itemname,itemprice,capacity):
        self.itemname=itemname
        self.itemprice=itemprice
        self.no=no
        self.capacity=capacity

    def productname(self):
        return self.itemname
    def productprice(self):
        return self.itemprice
    def productno(self):
        return self.no
       
class user(object):
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
        self.cartlist={}
        
def addproduct(self,product):
    for a in self.product:
        cartlist={
                'no':product.no,
                'itemname':product.itemname,
                'itemprice':product.itemprice
                }
        self.product.append(cartlist)
print('{} has been added.'.format.append(item.name))

def addcustomer(self,user):
    for user in object:
        self.append(user.name)
        
class cart(dict):
    def buyproduct(product,user):
        print('enter the object',itemname)
        if itemname in product:
            cart.append(itemname)
            cart.append(itemprice)
        
def removeitem(self,itemname):
    for value in self.product:
        if value['itemname']==itemname:
            value[capacity]=None
            self.cart.remove(itemname)
    
    
        
        

        
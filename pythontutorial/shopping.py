# -*- coding: utf-8 -*-
choice = input("Are you a prime member (yes/no):")
amtPurchased = float(input(' Enter  amount purchased '))
print(choice,amtPurchased)
def netAmount(amtPurchased,choice):
    discount = 0
    shipping = 0
    netamt = 0
    
    if (amtPurchased >= 30000):
        discount = .3 * amtPurchased;
        shipping = 300
    elif (amtPurchased >20000 and amtPurchased <30000):
        discount = .2 * amtPurchased;
        shipping = 200
    elif (amtPurchased <=20000):
        discount = .1 * amtPurchased;
        shipping = 100
        
    if (choice == 'yes'):
        shipping = 0
    
    netamt = amtPurchased - discount + shipping
    
    return netamt

netamt = netAmount(amtPurchased,choice)

print('net amount ',netamt)
    
            
        


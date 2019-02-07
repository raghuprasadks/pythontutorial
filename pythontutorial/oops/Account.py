# -*- coding: utf-8 -*-
import random
class Account():
    def openAccount(self,name,address,idproof):
        print('Account:openAccount')
        self.name = name
        self.address = address
        self.idproof = idproof
        self.balance = 0
        self.accountNo = random.randint(1,100)
        return self.accountNo
    
    def deposit(self,acctNo,amount):
        print('Account:deposit')
        self.accountNo = acctNo
        self.balance = self.balance + amount
        return self.balance 
    
    def withdraw(self,acctNo,amount):
        print('Account:deposit')
        self.accountNo = acctNo
        if (self.balance > amount):
            self.balance = self.balance - amount
        else:
            print('You do not have enough balance')
        return self.balance 
    
    def checkBalance(self,acctNo):
        print('Account:deposit')
        self.accountNo = acctNo
        return self.balance 
    
    
myAcct = Account()
acctNo = myAcct.openAccount('Raghu','Jakkur','DL-1233')
print('Your account no is ',acctNo)
amt = 10000
balance = myAcct.deposit(acctNo,amt)
print('Your balance after deposit of  ',amt, 'is ',balance)
amt = 20000
balance = myAcct.deposit(acctNo,amt)
print('Your balance after deposit of  ',amt, 'is ',balance)

amt = 50000
balance = myAcct.deposit(acctNo,amt)
print('Your balance after deposit of  ',amt, 'is ',balance)

amt = 85000
balance = myAcct.withdraw(acctNo,amt)
print('Your balance after withdrawal of  ',amt, 'is ',balance)

amt = 50000
balance = myAcct.withdraw(acctNo,amt)
print('Your balance after withdrawal of  ',amt, 'is ',balance)


balance = myAcct.checkBalance(acctNo)
print('Your current balance is  ',balance)



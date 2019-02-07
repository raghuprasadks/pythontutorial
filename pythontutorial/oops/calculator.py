# -*- coding: utf-8 -*-
class calculator():
    def addition(self,num1,num2):
        return num1+num2    
    def subtraction(self,num1,num2):
        return num1-num2    
    def multiplication(self,num1,num2):
        return num1*num2    
    def division(self,num1,num2):
        return num1/num2    
def main():
    myCal = calculator()
    print(myCal.addition(100,10))
    res = myCal.subtraction(100,10)
    print('subtraction ',res )
    res = myCal.multiplication(100,10)
    print('multiplication ',res)
    res = myCal.division(100,10)
    print('Division ',res)
if __name__=="__main__":
    main()
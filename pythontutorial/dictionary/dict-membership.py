# -*- coding: utf-8 -*-

dict ={0:"Zero",1:"One",2:"Two",3:"Three"}
ans ="y"
while ans =='y' or ans=="Y":
    val = input("Enter Value")
    print ("Value",val,end=" ")
    for k in dict:
        if dict[k] == val:
            print("exists at ",k)
            break
    else:
        print("not found")
    ans =input("Want to check more values ?(y/n) :")
    



# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:05:19 2018

@author: Raghu Prasad
"""
def forLoopWithContinue():
    x=0
    mylist = [8,9]
    for x in range(1,11):
        if(mylist[0]==x):            
            continue;
        print('For Loop with continue ',x)
forLoopWithContinue()

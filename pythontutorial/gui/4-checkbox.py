# -*- coding: utf-8 -*-

from tkinter import *
master = Tk() 
var1 = IntVar() 
Checkbutton(master, text='male', variable=var1,onvalue=1,offvalue=0).grid(row=0, sticky=W) 
print('variable 1- male ',var1)
var2 = IntVar() 
Checkbutton(master, text='female', variable=var2,onvalue=1,offvalue=0).grid(row=1, sticky=W) 
print('variable 2- female ',var2)
mainloop() 


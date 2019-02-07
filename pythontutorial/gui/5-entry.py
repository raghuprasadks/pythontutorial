# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import Label
from tkinter import Entry
master = Tk() 
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
mainloop() 

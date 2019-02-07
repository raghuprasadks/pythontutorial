# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox
top = tkinter.Tk()
def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()



import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button1 = tk.Button(r, text='Start', width=30, command=r.destroy)

 
button.pack() 
button1.pack()
r.mainloop() 


import tkinter as tk 
from tkinter import messagebox
r = tk.Tk() 
r.title('Buttons') 

def clickme(i):
   messagebox.showinfo( "Hello Python",  i+ " is clicked")

listbtn = ['First','Second','Third','Fourth']

count=0
for i in listbtn:
    listbtn[count] = tk.Button(r, text=i, width=25, command=lambda x=i:clickme(x))
    print('what is this button' , type(listbtn[count]))
    listbtn[count].pack()
    print('items are',i)
    count+=count
r.mainloop() 


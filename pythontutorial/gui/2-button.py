# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox
top = tkinter.Tk(className='Button Demo')
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



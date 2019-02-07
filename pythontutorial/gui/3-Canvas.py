# -*- coding: utf-8 -*-
import tkinter
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=315, fill="red")
C.pack()
top.mainloop()

from tkinter import *
master = Tk() 
w = Canvas(master, width=40, height=60) 
w.pack() 
canvas_height=20
canvas_width=200
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop() 


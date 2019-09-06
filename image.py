# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:44:15 2019

@author: Administrator
"""


import tkinter 
window = tkinter.Tk()
window.title("GUI")

icon = tkinter.PhotoImage(file = "C:\.png")

label  = tkinter.Label(window, image = icon)
label.pack()
label.mainloop()
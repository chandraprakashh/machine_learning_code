# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:35:02 2019

@author: Administrator
"""

import tkinter 
window = tkinter.Tk()
window.title("GUI")

def PrintOnClick():
        tkinter.Label(window, text = "welcome").pack()
        
tkinter.Button(window, text = "click me", command  = PrintOnClick).pack()
window.mainloop()
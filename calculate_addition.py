# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:26:23 2019

@author: Administrator
"""

import tkinter as tk
from functools import partial

def call_result(label_result,n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="result is %d" %  result)
    return

def call_result1(label_result,n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)-int(num2)
    label_result.config(text="result is %d" %  result)
    return

def call_result2(label_result,n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label_result.config(text="result is %d" %  result)
    return

def call_result3(label_result,n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)/int(num2)
    label_result.config(text="result is %d" %  result)
    return


root = tk.Tk()
root.geometry('400x200+100+200')
root.title('calculator-addition')
 
number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = tk.Label(root, text="calculator-addition").grid(row=0, column=2)

labelNum1 = tk.Label(root, text="enter a number").grid(row=1, column=0)
labelNum1 = tk.Label(root, text="enter another number").grid(row=2, column=0)

labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)

labelResult = tk.Label(root)
labelResult.grid(row=7, column=3)

labelResult = tk.Label(root)
labelResult.grid(row=7, column=4)

labelResult = tk.Label(root)
labelResult.grid(row=7, column=5)

enterNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
enterNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

call_result = partial(call_result, labelResult, number1, number2)
call_result1 = partial(call_result1, labelResult, number1, number2)
call_result2 = partial(call_result2, labelResult, number1, number2)
call_result3 = partial(call_result3, labelResult, number1, number2)

buttonCal = tk.Button(root, text="sumiition", command=call_result).grid(row=3, column=0)
buttonCal1 = tk.Button(root, text="subtrution", command=call_result1).grid(row=4, column=0)
buttonCal2 = tk.Button(root, text="multiplayy", command=call_result2).grid(row=5, column=0)
buttonCal3 = tk.Button(root, text="divaiddddi", command=call_result3).grid(row=6, column=0)
root.mainloop()








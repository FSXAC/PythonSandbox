# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:02:38 2016

@author: Muchen
"""

import tkinter as tk

root = tk.Tk()

# function to call
def printToConsole(event):
    print("Hello World!")
    
# different function for different events
def leftClick(event):
    print("left clicked")
    
def rightClick(event):
    print("right clicked")
    
def middleClick(event):
    print("Middle clicked")
    
    
button1 = tk.Button(root, text = "CLICK BELOW")
frame1 = tk.Frame(root, width = 300, height = 200)

# use '.bind("<event button>", function)
button1.bind("<Button-1>", printToConsole)
frame1.bind("<Button-1>", leftClick)
frame1.bind("<Button-2>", middleClick)
frame1.bind("<Button-3>", rightClick)

button1.pack()
frame1.pack()

root.mainloop()
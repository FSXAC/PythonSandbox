# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:25:30 2016

@author: Muchen
"""

import tkinter as tk

root = tk.Tk()

# top display fraame
displayFrame = tk.Frame()
displayFrame.pack(side = "top", fill = "both")

testBtn = tk.Button(displayFrame, text = "HELLO")
testBtn.pack(fill = "both")

root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:20:28 2016

@author: Muchen
"""

# import gui lib
import tkinter

# create blank window
root = tkinter.Tk()

# create text using Label(window, text)
textLabel = tkinter.Label(root, text = "TESTING TEST HERE")

# pack it in the window
textLabel.pack()

# continuously display until user clicks it off
root.mainloop()
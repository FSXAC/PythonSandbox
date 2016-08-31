# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:00:19 2016

@author: Muchen
"""

# import gui lib
import tkinter as tk

# create window
root = tk.Tk()

# create top frame
topFrame = tk.Frame(root)
topFrame.pack()

# create bottom frame
btmFrame = tk.Frame(root)
btmFrame.pack(side = tk.BOTTOM)

# buttons: Button(where it is, what to show, fg = text color)
button1 = tk.Button(topFrame, text = "BUTTON 1", fg = "red")
button2 = tk.Button(topFrame, text = "BUTTON 2", fg = "blue")
button3 = tk.Button(btmFrame, text = "BUTTON 3", fg = "green")
button4 = tk.Button(btmFrame, text = "BUTTON 4", fg = "purple")

# pack the buttons to show it on the frame
button1.pack(side = tk.LEFT)
button2.pack(side = tk.RIGHT)
button3.pack(side = tk.LEFT)
button4.pack(side = tk.RIGHT)

# continuously display until user clicks it off
root.mainloop()
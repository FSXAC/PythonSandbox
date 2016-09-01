# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:39:34 2016

@author: Muchen
"""

import tkinter as tk
import tkinter.messagebox as tkmb

def testFunction():
    print("TEST!!!")

root = tk.Tk()

# === MESSAGEBOX ===
def showInfo():
    # type 1: basic text (alertbox)
    tkmb.showinfo('Window title', 'Text displayed for the user')

def askQuestion():
    # type 2: has options
    response = tkmb.askquestion('Window title', 'Yes or no?')
    print("YOUR RESPONSE:", response)

# === MENU ===
# create menu
menu = tk.Menu(root)

# config root menu to 'menu' obj
root.config(menu = menu)

# create dropdown submenu placed inside main menu
submenu = tk.Menu(menu)
menu.add_cascade(label = "File", menu = submenu)

# add elements inside the drop down menu
submenu.add_command(label = "New", command = testFunction)
submenu.add_command(label = "Open", command = testFunction)

# create separator
submenu.add_separator()
submenu.add_command(label = "Exit", command = root.destroy)

# another item in main menu
submenu2 = tk.Menu(menu)
menu.add_cascade(label = "Edit", menu = submenu2)
submenu2.add_command(label = "Undo", command = testFunction)

# === TOOLBAR ===
# create frame for toolbar
toolbar = tk.Frame(root, bd = 1, relief = 'sunken')

# create button for the toolbar
toolbarBtn1 = tk.Button(toolbar, text = "Info", 
                        command = showInfo)

# add button to the toolbar frame
toolbarBtn1.pack(side = 'left', padx = 2, pady = 2)

# creating another button
toolbarBtn2 = tk.Button(toolbar, text = "Question", 
                        command = askQuestion)
toolbarBtn2.pack(side = 'left', padx = 2, pady = 2)

# pack and display the toolbar
toolbar.pack(side = 'top', fill = 'x')

# === STATUS BAR ===
# create label as status bar located in root with bd (border)
statusbar = tk.Label(root, text = "Ready", bd = 1, 
                     relief = 'sunken', anchor = 'w')
statusbar.pack(side = 'bottom', fill = 'x')

# === CANVAS ===
# create canvas object and pack it into the root window
canvas = tk.Canvas(root, width = 300, height = 200, 
                   bd = 1, relief = 'sunken')
canvas.pack()

# lines (x1, y1, x2, y2)
line1 = canvas.create_line(0, 0, 100, 100)
line2 = canvas.create_line(100, 100, 200, 0, fill = 'red')

# rectangles (top-left, btm-right)
rect1 = canvas.create_rectangle(25, 100, 150, 150, fill = '#ABC')

# deleting graphics
canvas.delete(line2)

root.mainloop()
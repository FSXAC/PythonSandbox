# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:50:44 2016

@author: Muchen
"""

import tkinter as tk

root = tk.Tk()

# some things to organize
label1 = tk.Label(root, text = "ID")
label2 = tk.Label(root, text = "Password")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
checkbutton1 = tk.Checkbutton(root, text = "Remember me")
button1 = tk.Button(root, text = "Submit")

# instead of packing, we use grid layout

# stack the labels on top of each other
# column defaults to 0
# align text using 'sticky = "n/e/s/w/ne/se..."'
label1.grid(row = 0, sticky = "e")
label2.grid(row = 1, sticky = "e")

# put the entry to the right
entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

# widget that uses multiple grids - use 'columnspan'
checkbutton1.grid(columnspan = 2)
button1.grid(columnspan = 2)

root.mainloop()
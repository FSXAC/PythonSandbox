#### Python GUI TkInter Program ####
#### Mansur He 2014 - 09 - 20   ####

import sys
from tkinter import *
from tkinter import ttk

gui = Tk()

gui.geometry("500x500+400+200")

label = Label(text = "HELLO WORLD", fg = "white", bg = "black").place(x = 0, y = 0)

gui.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:25:30 2016

@author: Muchen
"""

import tkinter as tk

root = tk.Tk()

# top buttons
topFrame = tk.Frame(root)
button_select = tk.Button(topFrame, text = "Select HW Module")
button_quit = tk.Button(topFrame, text = "Quit", command = root.destroy)

button_select.pack(side = "left")
button_quit.pack(side = "left")
topFrame.pack()

# row buttons
midFrame = tk.Frame(root)
button_trace = tk.Button(midFrame, text = "Trace Signal")
button_trace_settings = tk.Button(midFrame, text = "Trace Signal Settings")
button_settings = tk.Button(midFrame, text = "HW Module Settings")

button_trace.pack(side = "left")
button_trace_settings.pack(side = "left")
button_settings.pack(side = "left")

midFrame.pack()

# bottom frame
btnFrame = tk.Frame(root, relief = "sunken")

# display
display = tk.Canvas(btnFrame, width = 200, height = 80, bd =1, relief = "sunken")
display.pack(side = "left")

# input panel
panel = tk.Frame(btnFrame, relief = "sunken")
label1 = tk.Label(text = "switch #0")
label2 = tk.Label(text = "switch #1")
button_switch1_on = tk.Button(panel, text = "on")
button_switch1_off = tk.Button(panel, text = "off")
button_switch2_on = tk.Button(panel, text = "on")
button_switch2_off = tk.Button(panel, text = "off")

label1.pack()
button_switch1_on.pack(side = "left")
button_switch1_off.pack(side = "left")
label2.pack()
button_switch2_on.pack(side = "left")
button_switch2_off.pack(side = "left")
panel.pack()

btnFrame.pack()

root.mainloop()
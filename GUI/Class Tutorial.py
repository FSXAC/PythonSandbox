# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:14:38 2016

@author: Muchen
"""
#TODO: thenewboster tut9

import tkinter as tk

class CustomButton:
    
    def __init__(self, master):
        
        # create master frame
        frame = tk.Frame(master)
        frame.pack()
        
        # create everthing else like normal
        self.printButton = tk.Button(
        frame, text = "Print message", command = self.printMsg)
        self.printButton.pack(side = "left")
        
        # use 'master.destory' to close the entire window
        self.quitButton = tk.Button(
        frame, text = "Quit", command = master.destroy)
        self.quitButton.pack(side = "left")
        
    def printMsg(self):
        print("The button is clicked on!")

root = tk.Tk()
cb1 = CustomButton(root)
cb2 = CustomButton(root)
root.mainloop()
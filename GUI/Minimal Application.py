# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:17:19 2016

@author: Muchen
"""

import tkinter as tk

# application window
class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        
        # setup frame
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.quitButton = tk.Button(self, text = "Quit", command = self.quit)
        self.quitButton.grid()

app = Application()

app.master.title("sample application")
app.mainloop()
# -*- coding: utf-8 -*-
"""
Fun with join function

Created on Mon Aug  8 17:38:59 2016

@author: Muchen
"""

# prints some numbers joined with '.'
a = ".".join(str(x) for x in range(0, 255, 51))
print(a)

# prints a list
b = ".".join(["1", "2", "3", "4"])
print(b)
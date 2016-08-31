# -*- coding: utf-8 -*-
"""
List filter
Created on Mon Aug  8 17:31:46 2016

@author: Muchen
"""

def listFilter(inputList, elementType):
    good = []
    bad = []
    for element in inputList:
        if type(element) is elementType:
            good.append(element);
        else:
            bad.append(element)
            
    return good, bad
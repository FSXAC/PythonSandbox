# Library of userful functions

import pygame
import random
import time
import os

def falseInput(message):
    print("\n", message, "\n")

def getFloatInput(message):
    """ This function will ask for a float, it will keep looping
        when user gives an invalid input, loop ends and returns
        the value when a valid input was given """
    while True:
        uInput = input(message)
        try:
            uInput = float(uInput)
            break
        except:
            falseInput("<<< INVALID INPUT >>>")
    return uInput

def getIntInput(message):
    """ This function is similar to getFloatInput function,
        except that it will check and return a integer instead
        of a float """
    while True:
        uInput = input(message)
        try:
            uInput = int(uInput)
            break
        except:
            falseInput("<<< INVALID INPUT >>>")
    return uInput

def containsPoint(x, y, rect_x, rect_y, rectWidth, rectHeight):
    """ This function checks whether if a point is within a rectangle"""
    """ (pointer's x position, pointer's y position,
        rectangle's starting x position, rectangle's starting y position,
        rectangle width, and rectangle height) """
    if x in range(rect_x, (rect_x + rectWidth + 1)) and y in range(rect_y, (rect_y + rectHeight + 1)):
        return True
    else:
        return False

# The geometry assignment
# Use chooses can find the area, volume, or primeter of a shape
# last edited by Mansur

# imports
import math
import pygame

# FUNCTION DEFININGS
def intro():
    print( \
          """This is a geometry program.
Select a shape, enter the values, and results will be shown""")

# Menus
def getMeasure():
    separate(True)
    return str(input(\
        """[0] - Quit\n
[1] - Area
[2] - Volume
[3] - Perimeter \n
[INPUT] > """)).lower()

def getShapeA():
    separate(True)
    return str(input(\
        """[0] - Back\n
[1] - Rectangle
[2] - Rectanglular Prism
[3] - Circle
[4] - Sphere
[5] - Triangle
[6] - Cylinder
[7] - Cone
[8] - Hexagon\n
[INPUT] > """)).lower()

def getShapeV():
    separate(True)
    return str(input(\
        """[0] - Back\n
[1] - Rectangular Prism
[2] - Sphere
[3] - Cylinder
[4] - Cone\n
[INPUT] > """)).lower()

def getShapeP():
    separate(True)
    return str(input(\
        """[0] - Back\n
[1] - Rectangle
[2] - Circle
[3] - Right-Angle Triangle
[4] - Hexagon
[INPUT] > """)).lower()

# ================ Get variables
# returns any float value
def getVar(ask, var = 0): 
    while True:
        try:
            var = float(input(ask))
            break
        except:
            inIn()
    return var   
# ===============================

# Utility functions
# displays the answer with given arguments
def answer(measure, shape, result, unit = ""):
    separate()
    print("The", measure, "for the", shape, "is", result, "units", unit)
    input("\nPress the enter key to continue")

# displays invalid input by default, can be changed using arguments
def inIn(text = "\n<<<Invalid Input>>>"):
    print(text)

# draws a line that separates
def separate(newline = False):
    if newline == False:
        print("=============================================================================")
    else:
        print("=============================================================================\n")

# calculation functions
def rectArea():
    print(answer("area", "rectangle", (getVar("\n[Length] > ") * getVar("\n[Width] > ")), "squared"))

def rectPrismArea():
    length = getVar("\n[Length] > ")
    width = getVar("\n[Width] > ")
    height = getVar("\n[Height] > ")
    print(answer("surface area", "rectangular prism", (2 * ((length * height) + (length + width) + (height * width))), "squared"))

# Main program loop
separate()
intro()
while True:
    measure = getMeasure()
    if measure in "1 area":
        shape = getShapeA()
        if shape in "1 rectangle":
            rectArea()
        elif shape in "2 rectangular prism":
            rectPrismArea()
        elif shape in "3 circle":
            answer("area", "circle", ((getVar("\n[Radius] > ") ** 2) * math.pi), "squared")
        elif shape in "4 sphere":
            answer("surface area", "sphere", ((getVar("\n[Radius] > ") ** 2) * math.pi * 4), "squared")
        elif shape in "5 triangle":
            answer("area", "triangle", ((getVar("\n[Base] > ") * getVar("\n[Height] > ")) / 2), "squared")
        elif shape in "6 cylinder":
            height = getVar("\n[Height] > ")
            radius = getVar("\n[Radius] > ")
            answer("surface area", "cylinder", ((math.pi * (radius ** 2) * 2) + ((math.pi * (2 * radius)) * height)), "squared")
        elif shape in "7 cone":
            height = getVar("\n[Height] > ")
            radius = getVar("\n[Width] > ")
            answer("surface area", "cone", (math.pi * radius * (math.sqrt((radius ** 2) + (height ** 2)))), "squared")
        elif shape in "8 hexagon":
            answer("area", "hexagon", (6 * (0.5 * (getVar("\n[Side Length] > ") * getVar("\n[Radius] > ")))), "squared")
        elif shape in "0 back":
            continue
        else:
            inIn()
    elif measure in "2 volume":
        shape = getShapeV()
        if shape in "1 rectangular prism":
            answer("volume", "rectangular prism", (getVar("\n[Length] > ") * getVar("\n[Width] > ") * getVar("\n[Height] > "), "cubed"))
        elif shape in "2 sphere":
            answer("volume", "sphere", ((4/3) * math.pi * (calcRadius() ** 3)), "cubed")
        elif shape in "3 cylinder":
            answer("volume", "cylinder", (getVar("\n[Height] > ") * (2 * math.pi * (getVar("\n[Radius] > ") ** 2))), "cubed")
        elif shape in "4 cone":
            answer("volume", "cone", ((1/3) * (math.pi * getVar("\n[Height] > ") * (calcRadius() ** 2))), "cubed")
        elif shape in "0 back":
            continue
        else:
            inIn()
    elif measure in "3 perimeter":
        shape = getShapeP()
        if shape in "1 rectangle":
            answer("perimeter", "rectangle", (2 * (getVar("\n[Length] > ")+ getVar("\n[Width] > "))))
        elif shape in "2 circle":
            answer("perimeter / circumference", "circle", (2 * getVar("\n[Radius] > ") * math.pi))
        elif shape in "3 right-angle triangle":
            height = calcHeight()
            base = calcBase()
            answer("perimeter", "right-angle triangle", (math.sqrt((height ** 2) + (base ** 2)) + height + base))
        elif shape in "4 hexagon":
            answer("perimeter", "hexagon", (getVar("\n[Side Length] > ") * 6))
        elif shape in "0 back":
            continue
        else:
            inIn()
    elif measure in "0 quit":
        break
    else:
        inIn()

# Ending
input("\n\nThanks for using this program")
quit()

import math
import turtle

class Graph():
    def __init__(self):
        # Class variables
        self.screen = turtle.Screen()
        self.drawerTurtle, self.gridTurtle, self.axisTurtle = turtle.Turtle(visible = False), turtle.Turtle(visible = False), turtle.Turtle(visible = False)

        # Class variable modifications
        self.screen.bgcolor("black")

        # lift pen for all turtles
        self.drawerTurtle.penup()
        self.gridTurtle.penup()
        self.axisTurtle.penup()

        self.drawerTurtle.pencolor("red")
        self.gridTurtle.pencolor("grey")
        self.axisTurtle.pencolor("white")

        self.drawerTurtle.speed(100)
        self.gridTurtle.speed(100)
        self.axisTurtle.speed(100)

        # calls some other functions
        self.setupGrid()
        self.setupAxis()

        print("constructor finished")

    def setupAxis(self):
        # X AXIS
        # setup initial positions
        self.axisTurtle.goto(-500,0)
        self.axisTurtle.pendown()

        # draw across the screen
        self.axisTurtle.goto(500,0)
        self.axisTurtle.penup()

        # Y AXIS
        # setup initial positions
        self.axisTurtle.goto(0, -500)
        self.axisTurtle.pendown()

        # draw across the screen
        self.axisTurtle.goto(0, 500)
        self.axisTurtle.penup()

        print("axis setup completed")
        return True

    def setupGrid(self):
        step = 100

        # Create grid
        for i in range(-500, 500, step):
            print(i)
            self.gridTurtle.goto(-500, i)
            self.gridTurtle.pendown()
            self.gridTurtle.goto(500, i)

            self.gridTurtle.penup()

            self.gridTurtle.goto(i, -500)
            self.gridTurtle.pendown()
            self.gridTurtle.goto(i, 500)

            self.gridTurtle.penup()

        print("grid setup completed")
        return True

    def draw(self, equation = "x"):
        for x in range(-500, 500, 1):
            # TRY in case of invalid calculations
            try:
                y = eval(equation)
            except:
                ""
                #print("y at x=", x, "does not exist")

            # move the turtle and draw the trail
            self.drawerTurtle.goto(x, y)
            self.drawerTurtle.pendown()

            #print("x=", x, "\ty=", y)

        self.drawerTurtle.penup()

        print("function drawn")
        return True

    def clearScreen(self):
        self.screen.clear()
        return True

class Main():
    def __init__(self):
        # object and var setup
        self.grapher = Graph()

        # The program will always ask for a function / equation
        while True:
            userInput = input("EQUATION: y=")
            print("y=" + userInput)

            # analyse user input

            # see if it's valid
            equationIsValid = self.validateEquation(userInput)

            # if it is, do calculations and plot the graph
            if equationIsValid: self.plotEquation(userInput)
            else: print("SYNTAX ERROR")

    def validateEquation(self, equation):
        """This will take entered equation and see if it is correct or not"""
        return True

    def breakEquation(self, equation):
        """This will break the equation into smaller parts that Python IDE can then do math on"""
        return True

    def plotEquation(self, equation):
        """This will take the valid equation and plot it (y vs x)"""
        self.grapher.draw(equation)

Main()

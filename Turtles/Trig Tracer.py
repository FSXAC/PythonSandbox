import turtle
import math

spinnerH = 0
speed = 100
v = 4

screen = turtle.Screen()
screen.bgcolor("black")

spinner = turtle.Turtle(visible = True)
spinner.penup()
spinner.pencolor("white")
spinner.goto(-2.5, -57.3)

turtlex = turtle.Turtle(visible = False)
turtlex.penup()
turtlex.goto(-650, 0)
turtlex.pencolor("red")
turtlex.pendown()
turtlex.speed(speed)

turtlex2 = turtle.Turtle(visible = False)
turtlex2.penup()
turtlex2.goto(-650, 0)
turtlex2.pencolor("yellow")
turtlex2.pendown()
turtlex2.speed(speed)

turtley = turtle.Turtle(visible = False)
turtley.penup()
turtley.goto(0, 512)
turtley.pencolor("green")
turtley.pendown()
turtley.speed(speed)

turtley2 = turtle.Turtle(visible = False)
turtley2.penup()
turtley2.goto(0, 512)
turtley2.pencolor("blue")
turtley2.pendown()
turtley2.speed(speed)

spinnerMove = 0

while True:

    spinner.fd(5)
    spinnerH += 5
    if spinnerH == 360:
        spinnerH = 0

    turtlex.goto((((turtlex.pos())[0]) + v), (spinner.pos()[1]))
    turtlex2.goto((((turtlex2.pos())[0]) + v), (spinner.pos()[0]))
    turtley.goto((spinner.pos()[0]), (((turtley.pos())[1]) - v))
    turtley2.goto((spinner.pos()[1]), (((turtley2.pos())[1]) - v))
    if turtlex.pos()[0] >= 640:
        turtlex.penup()
        turtlex.goto(-650, (spinner.pos()[1]))
        turtlex.pendown()
    if turtlex2.pos()[0] >= 640:
        turtlex2.penup()
        turtlex2.goto(-650, (spinner.pos()[0]))
        turtlex2.pendown()
    if turtley.pos()[1] <= -512:
        turtley.penup()
        turtley.goto((spinner.pos()[0]), 512)
        turtley.pendown()
    if turtley2.pos()[1] <= -512:
        turtley2.penup()
        turtley2.goto((spinner.pos()[1]), 512)
        turtley2.pendown()
        

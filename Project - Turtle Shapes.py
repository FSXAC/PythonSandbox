import turtle
import time
 
screen = turtle.Screen()
screen.setup(width = 1.00, height = 1.00)
screen.bgcolor("black")
draw = turtle.Turtle(visible = False)
draw2 = turtle.Turtle(visible = False)
 
def drawCircle():
    for i in range(18):
        draw.fd(20)
        draw.lt(20)
 
def circle():
    draw.speed(0)
    draw.goto(0, 0)
    draw.pencolor("white")
    draw.pendown()
    for i in range(18):
        drawCircle()
        draw.left(20)
    draw.penup()
 
def square2():
    screen.bgcolor("black")
    draw.speed(0)
    draw2.speed(0)
    draw.goto(0, 0)
    draw2.goto(0, 0)
    draw.pendown()
    draw2.pendown()
    move = 1
    draw.pencolor("red")
    draw2.pencolor("yellow")
    for i in range(204):
        if draw.pencolor() == "red":
            draw.pencolor("blue")
        else:
            draw.pencolor("red")
        if draw2.pencolor() == "yellow":
            draw2.pencolor("green")
        else:
            draw2.pencolor("yellow")
        draw.fd(move)
        draw.rt(91)
        draw2.fd(move)
        draw2.lt(91)
        move += 5
    draw.penup()
    draw2.penup()
 
def square():
    draw.speed(0)
    draw.goto(0, 0)
    draw.pendown()
    move = 1
    draw.pencolor("red")
    for i in range(340):
        if draw.pencolor() == "red":
            draw.pencolor("cyan")
        else:
            draw.pencolor("red")
        draw.fd(move)
        draw.rt(91)
        move += 3
        draw.stamp()
    draw.penup()

def drawHexagon():
    draw.speed(0)
    draw.goto(0, 0)
    draw.pendown()
    draw.pencolor("purple")
    for i in range(6):
        draw.fd(60)
        draw.lt(60)

def hexagon():
    screen.bgcolor("white")
    for i in range(18):
        drawHexagon()
        draw.left(20)
        

def hexagon2():
    screen.bgcolor("black")
    draw.speed(0)
    draw.goto(0, 0)
    draw.pendown()
    move = 60
    draw.pencolor("purple")
    for i in range(340):
        draw.fd(move)
        draw.lt(61)
        move += 1

def stop():
    time.sleep(1)
    screen.clear()
    
circle()
stop()
square()
stop()
square2()
stop()
hexagon()
stop()
hexagon2()
stop()
screen.exitonclick()

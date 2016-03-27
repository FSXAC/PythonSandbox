__author__ = 'Mansur'
import turtle

class Main:
    def __init__(self):
        screen = turtle.Screen()
        screen.bgcolor("black")

        heading = 45
        targetDistance = 50
        distance = 0
        speed = 5
        latency = 4

        spinner = turtle.Turtle(visible = True)
        spinner.penup()
        spinner.pencolor("white")
        spinner.goto(-300, 0)
        spinner.setheading(heading)
        spinner.speed(100)
        spinner.pendown()

        drawer = turtle.Turtle(visible= True)
        drawer.penup()
        drawer.pencolor("orange")
        drawer.goto(-500, 0)
        drawer.speed(100)
        drawer.pendown()

        isRunning = True

        while isRunning:
            spinner.fd(speed)
            distance += speed

            if distance >= targetDistance:
                heading += 90
                spinner.seth(heading)
                distance = 0

            if heading == 405:
                heading = 45

            drawer.goto(((drawer.pos()[0] + latency), spinner.pos()[1]))

            if drawer.pos()[0] >= 500:
                drawer.penup()
                drawer.goto(-500, spinner.pos()[1])
                drawer.pendown()

Main()
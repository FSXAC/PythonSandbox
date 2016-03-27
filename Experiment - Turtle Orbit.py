import turtle

speed = 0

screen = turtle.Screen()
screen.bgcolor("black")

sun = turtle.Turtle(visible = False)
sun.speed(speed)
sun.penup()

earth = turtle.Turtle()
earth.shape("circle")
earth.shapesize(0.5, 0.5, 1)

sun.goto(0, -50)
sun.color("black", "yellow")
sun.begin_fill()
sun.circle(50)
sun.end_fill()

sun.goto(0, -40)
sun.color("white", "white")
sun.begin_fill()
sun.circle(40)
sun.end_fill()

earth.goto(0, -80.2)
earth.pencolor("green")

while True:
    earth.fd(7)
    earth.lt(5)

screen.exitonclick()

import turtle
import math
import random

wn = turtle.Screen()

a = wn.window_height()
b = wn.window_width()
print(a, b)

ball = turtle.Turtle()

v = 0
ball.hideturtle()
ball.goto(0, 300)
ball.right(90)

ball.showturtle()
for i in range(100):
    turtle.forward(v)
    v += 1

wn.exitonclick()

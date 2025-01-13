##Creating the turtle

import turtle as t
import random

##Setting the turtle's start point

t.goto(0,0)

##Colors/movement

angles = [0, 90, 270]
colors = ["red","orange","yellow","green","blue","purple"]
for i in range (100000000000000):
    t.speed(0)
    t.color(colors[i%6])
    t.forward(5)
    t.right(random.choice(angles))

    if t.xcor() > 400:
        t.penup()
        t.goto(0,0)
        t.pendown()

    if t.ycor() > 400:
        t.penup()
        t.goto(0,0)
        t.pendown()

if t.xcor() > -400:
        t.penup()
        t.goto(0,0)
        t.pendown()

if t.ycor() > -400:
        t.penup()
        t.goto(0,0)
        t.pendown()

turtle.exitonclick()
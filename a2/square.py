import turtle
import random

turtle.setup(width = 600, height = 600)
screen = turtle.Screen()

t = turtle.Turtle()
t.shape(name = 'turtle')
t.speed(5)
t.color()
t.seth(90)

squares = 20
width = screen.window_width()/2
height = screen.window_height()/2
for x in range(squares):
    t.up()
    if (x%2 == 0):
        t.goto(width,height)
        t.down()
        t.goto(-width,height)
        t.goto(-width,-height)
        t.goto(width,-height)
        t.goto(width,height)
        t.up()
    else:
        t.goto(width,0)
        t.down()
        t.goto(0,height)
        t.goto(-width,0)
        t.goto(0,-height)
        t.goto(width,0)
        t.up()
        width = width / 2
        height = height/2

t.goto(100,100)

screen.exitonclick()
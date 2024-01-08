import turtle
import random

turtle.setup(width = 600, height = 600)
screen = turtle.Screen()

t = turtle.Turtle()
t.shape(name = 'turtle')
t.speed(40)
t.color()
t.seth(90)

def turtColor():
    r = random.uniform(0,1)
    g = random.uniform(0,1)
    b = random.uniform(0,1)
    return (r,g,b)

#flowers
t.width(width=None)
t.fd(100)
t.up()

t.goto(-225,-100)
t.fillcolor('blue')
t.begin_fill()
for _ in range(4):
    t.fd(200)
    t.right(20)
    t.back(200)
    t.right(20)
t.end_fill()
t.down()

t.up()
t.goto(-75,-100)
t.down()

t.up()
t.goto(75,-100)
t.down()

t.up()
t.goto(225,-100)
t.down()



screen.exitonclick()
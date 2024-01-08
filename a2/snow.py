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

def snow(size, arms, seg):
    t.color(turtColor())
    t.up()
    x = random.uniform(-(screen.window_width()/2)+50,screen.window_width()/2-50)
    y = random.uniform(-(screen.window_height()/2)+50,screen.window_height()/2-50)
    t.goto(x,y)
    t.down()
    t.seth(random.uniform(-180,180))
    for _ in range(arms):
        for _ in range(seg):
            t.right(30)
            t.fd(size)
            t.back(size)
            t.left(60)
            t.fd(size)
            t.back(size)
            t.right(30)
            t.fd(size)
        t.back(size*seg)
        t.right(360/arms)

for _ in range(30):
    arms = random.randint(2,12)
    size = random.uniform(5,30)
    segment = random.randint(1,4)
    snow(size,arms,segment)

screen.exitonclick()
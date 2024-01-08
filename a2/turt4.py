import turtle

turtle.setup(width = 600, height = 600)
screen = turtle.Screen()

t = turtle.Turtle()
t.shape(name = 'turtle')
t.speed(20)
t.color()
t.seth(90)
def snow(x,y,h):
    t.up()
    t.goto(x,y)
    t.seth(h)
    t.down()
    for y in range(8):
        for x in range(4):
            t.right(45)
            t.fd(30)
            t.back(30)
            t.left(90)
            t.fd(30)
            t.back(30)
            t.right(45)
            t.fd(30)
        t.back(120)
        t.right(45)


snow(0,0,20)
snow(200,200,30)
screen.exitonclick()


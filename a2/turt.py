import turtle
import random

# edit this line to control where window appears
turtle.setup(width=600, height=600)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)
turtle.speed(20)
turtle.shape(name="turtle")

def loops():
    for x in range(150):
        turtle.right(random.randint(100,150))
        turtle.forward(200)
        change_color()

screen = turtle.Screen()

def up():
    turtle.setheading(90)
    turtle.forward(100)
 
 
def down():
    turtle.setheading(270)
    turtle.forward(100)
 
 
def left():
    turtle.setheading(180)
    turtle.forward(100)
 
 
def right():
    turtle.setheading(0)
    turtle.forward(100)

turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
 
turtle.mainloop()


screen.exitonclick()
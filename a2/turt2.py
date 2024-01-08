import turtle

turtle.setup(width = 600, height = 600)
screen = turtle.Screen()

t = turtle.Turtle()
t.shape(name = 'turtle')
t.speed(10)



t.color(0,.2,.3)









for x in range(200):
    t.forward(x*1.3+5)
    t.right(119.5)

screen.exitonclick()


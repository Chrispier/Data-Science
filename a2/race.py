import turtle
import random

turtle.setup(width = 600, height = 600)
screen = turtle.Screen()

ref = turtle.Turtle()
ref.color('black')
ref.speed(300)

for x in range(10):
    ref.up()
    ref.goto(-175+(x*25),-75)
    ref.down()
    ref.seth(90)
    for y in range(10):
        ref.fd(10)
        ref.up()
        ref.fd(10)
        ref.down()
    ref.up()
    ref.left(90)
    ref.fd(4)
    ref.write(x+1, font=("Arial", 16, "bold"))
ref.up()
ref.goto(-175+(10*25),-75)
ref.down()
ref.seth(90)
ref.fd(200)
ref.right(90)
ref.fd(1)
ref.right(90)
ref.fd(200)
ref.up()
ref.goto(-100,225)

t1 = turtle.Turtle()
t1.shape(name = 'turtle')
t1.speed(40)
t1.color('red')
t1.up()
t1.goto(-200,100)

t2 = turtle.Turtle()
t2.shape(name = 'turtle')
t2.speed(40)
t2.color('blue')
t2.up()
t2.goto(-200,50)

t3 = turtle.Turtle()
t3.shape(name = 'turtle')
t3.speed(40)
t3.color('green')
t3.up()
t3.goto(-200,0)

t4 = turtle.Turtle()
t4.shape(name = 'turtle')
t4.speed(40)
t4.color('purple')
t4.up()
t4.goto(-200,-50)


for _ in range(999):
    t1move = random.randint(2,6)
    t2move = random.randint(2,6)
    t3move = random.randint(2,6)
    t4move = random.randint(2,6)
    t1.fd(t1move)
    t2.fd(t2move)
    t3.fd(t3move)
    t4.fd(t4move)
    if t1.xcor()>75:
        ref.write('T1 Wins',font=("Arial", 16, "bold"))
        break
    if t2.xcor()>75:
        ref.write('T2 Wins',font=("Arial", 16, "bold"))
        break
    if t3.xcor()>75:
        ref.write('T3 Wins',font=("Arial", 16, "bold"))
        break
    if t4.xcor()>75:
        ref.write('T4 Wins',font=("Arial", 16, "bold"))
        break



screen.exitonclick()
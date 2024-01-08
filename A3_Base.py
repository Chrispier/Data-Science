import turtle
import random
import time
random.seed(50)

#Setting up the screen
screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
#Name for the window that is opened
screen.title('Bubble Sort')
turtle.speed(0)
turtle.hideturtle()

# This function draws a bar at the specified x and y coordinate with width w and height h
def draw_bar(x,y,w,h):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

# Draws n bars using height values and order from list v
def draw_bars(v,n):
    x = -400
    w = 800/n
    for  i in range(n):
        draw_bar(x,-400,w,v[i])
        x += w

# Takes in list v and sorts it
def bubble_sort(v,draw):
    """
    You are given list v of random integers. It is not given the size or range of values.
    Implement the BubbleSort algorithm below to sort v.
    After every iteration of the loop, add the following three lines of code so 
    the sorting algorithm can be visualized.

    turtle.clear()
    draw_bars(v,n)
    screen.update()

    """
    #TODO 1: Write your code here. Make sure to delete 'pass' once you start writing your code
    for x in range(len(v)-1):
        for index in range(len(v)-x-1):
            if(v[index]>v[index+1]):
                temp = v[index]
                v[index] = v[index+1]
                v[index + 1]=temp
                if(draw):
                    turtle.clear()
                    draw_bars(v,n)
                    screen.update()
    pass
    #end TODO 1: Don't write beyond this
    

# the number of values in the list
n = 50

# Creates an empty list and then fills it with random values
v = [0] * n
for i in range(n):
    v[i] = random.randint(1,800)

#TODO 2: Implement a way to measure time.
#Write your code in the space below
t1 = time.time()
bubble_sort(v,False)
t2 = time.time()
print(t2-t1)

#End TODO 2: Dont write beyond this.
screen.exitonclick()
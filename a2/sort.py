import turtle
import random
import time

screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
screen.title('Quick Sort Animation - PythonTurtle.Academy')
turtle.speed(0)

def draw_bar(x,y,w,h):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
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

def draw_bars(v,n,currenti=-1,currentj=-1):
    turtle.clear()
    x = -400
    w = 800/n
    for  i in range(n):
        if i == currenti: turtle.fillcolor('red')
        elif i == currentj: turtle.fillcolor('blue')
        else: turtle.fillcolor('gray')
        draw_bar(x,-400,w,v[i])
        x += w
    screen.update()

def partition(v,x,y):
    p = random.randint(x,y)
    v[p], v[y] = v[y], v[p]
    pivot = v[y]
    i, j = x, y-1
    while i <= j:
        while v[i] <= pivot and i <= j:
            draw_bars(v,n,i,j)
            i += 1
        while v[j] > pivot and j >= i:
            draw_bars(v,n,i,j)
            j -= 1
        if i < j:
            draw_bars(v,n,i,j)
            v[i], v[j] = v[j], v[i]
    v[i], v[y] = v[y], v[i]
    draw_bars(v,n,i,y)
    return i

def quick_sort(v,x,y):
    if x >= y:
        return
    m = partition(v,x,y)
    quick_sort(v,x,m-1)
    quick_sort(v,m+1,y)

def insert(v,k):
    x = v[k]
    for i in range(k-1,-1,-1):
        if v[i] > x: v[i+1] = v[i]
        else:
            v[i+1] = x
            return
        turtle.clear()
        draw_bars(v,n)
        screen.update()
    v[0] = x
    
def insertion_sort(v,k):
    if k == 1: return
    insertion_sort(v,k-1)
    insert(v,k-1)

def bubble_sort(v):
    # Write your code here. Make sure to delete 'pass' once you want to test the code

    pass
    for x in range(len(v)):
        for index in range(len(v)-x-1):
            if(v[index]>v[index+1]):
                temp = v[index]
                v[index] = v[index+1]
                v[index + 1]=temp
                turtle.clear()
                draw_bars(v,n)
                screen.update()
    
n = 50
v = [0] * n
for i in range(n):
    v[i] = random.randint(1,800)

t1 = time.time()
quick_sort(v,0,n-1)
turtle.clear()
draw_bars(v,n,-1)
turtle.update()
t2 = time.time()
print('elapsed time=', t2-t1)
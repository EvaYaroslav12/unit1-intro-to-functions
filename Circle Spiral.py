import turtle
from turtle import *
t = Turtle()

t.color("blue")
t.speed(20)

sidelength = 100
rotate = 90
def Square(x,y):
    for i in range(1):
        t.circle(x)
        t.left(y)

def spinn(iRange):
    length = 5
    for i in range(iRange):
        Square(length, 5)
        length += 5
        
spinn(80)

turtle.done()

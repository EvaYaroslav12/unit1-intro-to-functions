import turtle
from turtle import *
t = Turtle()

turtle.colormode(255)
t.speed(90)

sidelength = 100
rotate = 90
def triangle(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def doubleCircles(iRange):
    length = 5
    r = 0
    g = 0
    b = 0
    c = 1
    m = 0
    y = 0
    degree = 5
    for i in range(iRange):
        triangle(length, 90)
        length += 2
        t.left(degree)
        t.pencolor(r,g,b)
        
        r += 12 * c
        b += 12 * m
        g += 12 * y
        if r > 240:
            c = -1
            m = 1
        if r < 0:
            c = 0
            r = 0
        if b > 240:
            m = -1
            y = 1
        if b < 0:
            b = 0
            m = 0
        if g > 240:
            y = -1
            c = 1
        if g < 0:
            g = 0
            y = 0

doubleCircles(240)

turtle.done()

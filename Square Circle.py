import turtle
from turtle import *
t = Turtle()

t.speed (20)

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(sidelength, rotate)


def addSquares(iRange):
    length = 100

    for i in range(iRange):
        square(length, 90) 
        t.left(5)
       
            

addSquares(72)

turtle.done()

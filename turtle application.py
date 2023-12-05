from turtle import *


def drawSquare(distance): #square drawing function
    for a in range(1,5):
        forward(distance)
        left(90)
hideturtle()
pensize(2)
x=int(input("enter square number:"))
x+=1
for a in range(x):
    drawSquare(50*a)
    
drawSquare(50)
drawSquare(100)
drawSquare(150)


for a in range(1,4):
    forward(200)
    rt(60)

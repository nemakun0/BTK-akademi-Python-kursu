from turtle import *
title ("Turkish Flag")
setup(width=600,height=400)
bgcolor("red")

def colorLocation(color1,x,y):
    penup()
    goto(x,y)
    pendown()
    color(color1)
    begin_fill()

def star():
    colorLocation("white",80,25)
    for i in range(5):
        forward(50)
        right(144)
        forward(50)
        right(-72)
    end_fill()
def moon(radius):
    circle (radius)
    end_fill()

colorLocation("white",-110,-120)
moon(130)
colorLocation("red",-70,-90)
moon(100)

star()
mainloop()














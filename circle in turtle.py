from turtle import *

pensize(10)
shape("blank")

fillcolor("grey")
begin_fill()
end_fill()

for x in range (2):
    forward(100)
    right(90)
    forward(250)
    right(90)
    
pencolor("red")

penup()
goto(50,-80)
pendown()
fillcolor("red")
begin_fill()
circle(30)
end_fill()

pencolor("yellow")
penup()
goto(50,-155)
pendown()
fillcolor("yellow")
begin_fill()
circle(30)
end_fill()

pencolor("green")
penup()
goto(50,-230)
pendown()
fillcolor("green")
begin_fill()
circle(30)
end_fill()

from turtle import *
n=int(numinput("polygon","number of edges:",5))
color=textinput("color","fill color:")
pensize(4)

begin_fill()
fillcolor(color)
circle(100,360,n)
end_fill()

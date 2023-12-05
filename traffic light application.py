from turtle import *
import time
w=Screen()
w.setup(300,700)
w.title("traffic light application")

penup()
goto(1,180)
pendown()
pensize(4)

for i in range (2):
    forward(80)
    right(90)
    forward(220)
    right(90)
def red():
    penup()
    goto(40,140)
    fillcolor("red")
    shape("circle")
    shapesize(3)

def yellow():
    penup()
    goto(40,70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)

def green():
    penup()
    goto(40,0)
    fillcolor("green")
    shape("circle")
    shapesize(3)

def brk():
    w.bye()
    
w.listen()
w.onkey(brk, "q")

while True:
    print("press Q to exit...")
    green()
    time.sleep(3)

    yellow()
    time.sleep(2)

    red()
    time.sleep(3)
        
   

w.mainloop()

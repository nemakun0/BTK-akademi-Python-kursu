from turtle import *
shape("turtle")
pensize(4)
w=Screen()
w.setup(500,500)
def turnLeft():
    left(90)
    write("I turned left")

def turnRight():
    right(90)
    write("I turned right")

def up():
    forward(10)

def down():
    backward(10)
w.onkeypress(turnLeft,"Left")
w.onkeypress(turnRight,"Right")
w.onkeypress(up,"Up")
w.onkeypress(down,"Down")

listen()#klavyeden gelen kodları dinler
w.mainloop()

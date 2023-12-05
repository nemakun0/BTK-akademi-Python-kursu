import turtle,time,random
size=[]
score=0
maxScore=0
#frame settings
w=turtle.Screen()
w.title("snake game")
w.setup(600,600)
w.colormode(255)
w.bgcolor(255,235,205)
w.tracer(0)#ekran güncelleme ayarları kapatılır

#the head of snake
sn=turtle.Turtle()
sn.speed(0)
sn.shape("circle")
sn.color("purple")
sn.penup()
sn.goto(0,0)
sn.direction="stop"

#food object
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(238,180,180)
food.penup()
food.goto(0,100)

def movement():
    if sn.direction=="up":
        y=sn.ycor() #y ekseninde yukarı git
        sn.sety(y+20)

    if sn.direction=="down":
        y=sn.ycor()# y ekseninde aşağı git
        sn.sety(y-20)

    if sn.direction=="right":
        x=sn.xcor()# x ekseninde sağa git
        sn.setx(x+20)

    if sn.direction=="left":
        x=sn.xcor()# y ekseninde aşağı git
        sn.setx(x-20)

def goUp():
    if sn.direction!= "down":
        sn.direction="up"
def goDown():
    if sn.direction!= "up":
        sn.direction="down"

def goRight():
    if sn.direction!= "left":
        sn.direction="right"

def goLeft():
    if sn.direction!= "right":
        sn.direction="left"

w.listen()
w.onkeypress(goUp,"Up")
w.onkeypress(goDown,"Down")
w.onkeypress(goRight,"Right")
w.onkeypress(goLeft,"Left")





def feed():
    global score
    global maxScore
    if sn.distance(food)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        food.goto(x,y)

        tail=turtle.Turtle()
        tail.speed(0)
        tail.shape("circle")
        tail.color(0,128,128)
        tail.penup()
        size.append(tail)
        
       
        score+=5
        if score>maxScore:
            maxScore=score
            w.title("score:{} high score{}".format(score,maxScore))

        sn.goto(sn.xcor(),sn.ycor())
            
    length= len(size)
    for indis in range(length-1,0,-1):
        x=size[indis-1].xcor()
        y=size[indis-1].ycor()
        size[indis].goto(x,y)
        
    if len(size)>0:
        x=sn.xcor()
        y=sn.ycor()
        size[0].goto(x,y)
        
def beginning():
    time.sleep(0.1)
    sn.goto(0,0)
    sn.direction="stop"
    
    for joint in size:
        joint.goto(1000,1000)
    size.clear()
    score=0
    w.title("score: {} high score:{}".format(score,maxScore))

while True:
    w.update()
    feed()
    movement()

    if sn.xcor() > 290 or sn.xcor() < -290 or sn.ycor() > 290 or sn.ycor() < -290:
        beginning()

    for joint in size:
        if joint.distance(sn) < 20:
            beginning()

    time.sleep(0.1)
     
w.mainloop()
        
    















        













        
    

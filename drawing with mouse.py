from turtle import *
pensize(3)
win=Screen()
win.setup(700,700)

def dot(x,y):
    goto(x,y)
    pendown()

win.onclick(dot)#tıklama yapıldığında dot fonksiyonunu çalıştır.

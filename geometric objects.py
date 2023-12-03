from math import *

class kup:
    def __init__(self,a):
        self.a=a

    def yAlan(self):
        return("yüzey alanı:",6*pow(self.a,2),"cm^2")

    def hacim(self):
        return("hacim:",pow(self.a,3),"cm^3")

class kure:
    def __init__(self,r):
        self.r=r
        
    def yAlan(self):
        return("yüzey alanı:",4*pi*pow(self.r,2),"cm^2'dir.")

    def hacim(self):
        return("hacim:",(4/3)*pi*pow(self.r,3),"cm^3")

class silindir:
    def __init__(self,r,h):
        self.r=r
        self.h=h

    def yAlan(self):
        return("yüzey alanı:",2*pi*self.r(self.r+self.h),"cm^2")#(2*pi*pow(r,2)+(2*pi*r*h))

    def hacim(self):
        return("hacim:",pi*pow(self.r,2)*h,"cm^3")

futbolTopu=kure(10)#futnol topu nesnesi
pinponTopu=kure(3)#parametresi yarıçapı temsil eder

kupseker=kup(2)
koli=kup(50)

merdane=silindir(3,30)
tencere=silindir(15,20)
lastik=silindir(35,20)

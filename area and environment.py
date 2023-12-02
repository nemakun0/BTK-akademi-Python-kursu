def area(l,w):
    a=l*w
    return a
def environment(l,w):
    e=2*(l+w)
    return e
l= int(input("enter the length of the rectangle:"))
w= int(input("enter the width of the rectangle:"))
print("the area of the rectangle :", area(l,w),"m^2")
print("the environment of the rectangle :", environment(l,w),"m")

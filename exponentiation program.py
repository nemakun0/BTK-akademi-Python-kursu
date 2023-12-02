def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1)
	
a= int(input("enter the base:"))
b= int(input("enter exponent:"))
print (ustel(a,b))

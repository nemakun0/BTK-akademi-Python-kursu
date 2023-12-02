l=[]
for i in range(0,6):
    number=int(input("enter a number:"))
    l.append(number)
l.sort()
print("median of list:",(l[2]+l[3])/2)

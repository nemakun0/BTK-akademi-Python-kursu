l=[]
c=1
for i in range(0,5):
    print("enter",c,". number:")
    number=int (input())
    l.append(number)
    c+=1
for i in range(0,5):
    print("l[",i,"]=",l[i])

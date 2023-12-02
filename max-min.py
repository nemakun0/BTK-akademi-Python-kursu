l=[]
total=0
for i in range(0,5):
    number=int (input("enter a number:"))
    l.append(number)
    total+=number
print("the sum of the smallest and largest numbers:",max(l)+min(l))
print("arithmetic mean:", total/len(l))

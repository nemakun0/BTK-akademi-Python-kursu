import random
print("10 question multiplication table test.")
score=0
for a in range(10):
    i=random.randint(1,10)
    x=random.randint(1,10)
    question="{}*{}=".format(i,x)

    answer=i*x
    reply=input(question)
    
    if int(reply)== answer:
        score+=1

print("number of correct:",score)
if score>8:
    print("very good")
elif score>6:
    print("good")
elif score >4:
    print("medium")
else:
    print("you should study more...")
    

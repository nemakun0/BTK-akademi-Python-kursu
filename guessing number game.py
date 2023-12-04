import random
number=random.randint(1,6)
guess=int(input("guess a number:"))
score=5
while True:
    if number==guess:
        print("you win:)\nyour score:",score)
        break
    else:
        print("you lose:(\nyour score:",score)
        score-=1
        guess=int(input("guess another number:"))

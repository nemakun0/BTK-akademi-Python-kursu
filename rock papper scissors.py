import random
list1=["Rock","Paper","Scissors"]
while True:
    out=int(input("Press 1 to start the game or 0 to exit."))
    if out==1:
        pc=random.choice(list1)#this choice belongs to pc
        player=input("[Rock-Paper-Scissors]").capitalize()
        print ("choice of computer is",pc)
        print("choice of player is",player)

        if pc==player:
            print("draw")
        if pc=="Paper" and player=="Rock":
            print("you lose")
        if pc=="Rock" and player=="Scissors":
            print("you lose")
        if pc=="Scissors" and player=="Paper":
            print("you lose")   
        if pc=="Paper" and player=="Scissors":
            print("you win")
        if pc=="Rock" and player=="Paper":
            print("you win")
        if pc=="Scissors" and player=="Rock":
            print("you win")
    elif out==0:
        break
    

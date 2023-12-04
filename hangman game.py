import random
scroll=["python","print","random","while","choice"]
word=random.choice(scroll)
man=['''
   +----+
   o    |
  /|\   |
  /     |
       ---''','''
   +----+
   o    |
  /|\   |
        |
       ---''','''
   +----+
   o    |
  /|    |
        |
       ---''','''
   +----+
   o    |
   |    |
        |
       ---''','''
   +----+
   o    |
        |
        |
       ---''','''
   +----+
        |
        |
        |
       ---''']
correctWord=[]
wrongWord=[]
claim=len(man)

while claim >0:
    out=""
    for h in word:
        if h in correctWord:
            out+=h
        else:
            out+="_"
    if out== word:
        break
    print("the word:",out)
    print(man[claim-1])
    enLetter=input()
    if  enLetter in correctWord or  enLetter in wrongWord:
        print( enLetter,"has already been entered")
    elif  enLetter in word:
        print("this letter is correct letter")
        correctWord.append(enLetter)
    else:
        print("this letter is a wrong letter.")
        claim-=1
        wrongWord.append(enLetter)
    

if claim!=0:
    print("the word:",word)
    print("Congratulations. You win...")
else:
    print("Unfortunately you lose...")
    print("the word was",word)

















 
 

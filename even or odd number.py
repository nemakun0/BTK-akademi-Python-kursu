user=input("please enter your user name: ")
password=input("please enter your password: ") 
if user=="admin" and password=="1234":
    print("welcome...")
else:
    print("unauthorized entry!")

#Is the entered number odd or even?
x= int(input("Enter the number you want to find out whether it is odd or even: "))
find = (x%2)
if find==0:
    print("the number that you entered is even")
else:
    print("the number that you entered is odd")
    

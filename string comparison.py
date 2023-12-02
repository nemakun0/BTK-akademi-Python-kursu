password="1234"
user="miranda"

u_entry=input("enter username:")
if u_entry==user:
    p_entry=input("enter password:")
    if p_entry==password:
        print("welcome...")
    else:
        print("incorrect password")
else:
    print("username is incorrect")
        


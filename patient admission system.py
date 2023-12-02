l=[]
while True:
    IN=int(input("please enter identification number:"))
    if IN in l:
        i=l.index(IN)
        print("examination order:",i+1)
    elif IN==0:
        print("who has the identification number",l[0],"enter the doctor's office.")
        l.pop(0)
    else:
        l.append(IN)
        print("Patient number",IN,"was queued")

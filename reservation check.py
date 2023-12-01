tableNo=0
resList=["jhon","hailey","alfa","miranda"]
resList2=["jacob","ashley"]
name=input("please enter the name that you make reservation: ")
if name=="jhon":
    tableNo=2
if name=="hailey":
    tableNo=3
if name=="alfa":
    tableNo=4
if name=="miranda":
    tableNo=1
if name in resList:
    print("You have a reservation at table",tableNo)
elif name in resList2:
    print("your reservation is not today")
elif name not in resList and name not in resList2:
    print("you do not have a reservation.")

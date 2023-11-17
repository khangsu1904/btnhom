cost=0
while True:
    age=input("Age:")
    if age=="":
        break
    age=int(age)
    if age<=0:
        print("Error\nPlease enter again")
        age=input("Age:")
    elif age<=2:
        cost=0
    elif age <=12:
        cost+=14
    elif age >=65:
        cost+=18
    else:
        cost+=23
if cost==0:
    print("There are no guests in the group")  
else:
    print("Total cost for the group is:",cost)

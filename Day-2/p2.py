a = int(input("Enter number of bill number"))
if(a<=150):
    print("your bill is ", 3*a)
elif(a>150 and a<301):
    print("Your bill is", 4*a)
else:
    print("Your bill is", 5*a)
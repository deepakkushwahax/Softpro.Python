num = int(input("Enter the Number: "))
for i in range(1,50):
    if (i % 3 == 0 and i % 5) == 0:
        print("fizzbuzz")
    elif (i % 3) == 0:
        print("fizz")
    elif (i % 5) == 0:
        print("buzz")
    else:
        print(i)

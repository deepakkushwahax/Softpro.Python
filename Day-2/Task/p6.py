for i in range(4):
    for j in range(5):
        if j == 0 or j == 4:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()


    for i in range(4):
        print("#", end=" ")
        for j in range(3):
            print("*", end=" ")
        print("#")

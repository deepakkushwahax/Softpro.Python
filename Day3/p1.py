from time import sleep
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print asterisks
    for k in range(i):
        print("* ", end="")

    print()

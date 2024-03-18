from time import sleep
number = int(input("Enter a number to print its multiplication table: "))
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")



for i in range(1,11):
    print("2 *",i,"=",2*i)
    sleep(1)
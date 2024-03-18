number = int(input("Enter the Number: "))
sum = 0
while(number>0):
    dig = number % 10
    sum = sum + dig
    number = number//10
print(sum)
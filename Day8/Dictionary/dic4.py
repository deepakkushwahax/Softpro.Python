# Write a program to take Dictionary as input and print the sum of values
dic1 = {}
n = int(input("Enter number of students: "))
for i in range(n):
    key = input("Enter Key: ")
    value = int(input("Enter the value: "))
    dic1[key] = value
sum = sum(dic1.values())
print("Sum of values:", sum)

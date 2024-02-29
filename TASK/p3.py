num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Comparing the numbers
if num1 > num2:
    print(num1, "is greater than", num2)
    print(num2, "is smaller than", num1)
elif num1 < num2:
    print(num2, "is greater than", num1)
    print(num1, "is smaller than", num2)
else:
    print("Both numbers are equal.")
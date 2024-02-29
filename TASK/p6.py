# Taking user input for a number
number = int(input("Enter a number: "))

# Checking if the number is prime or not
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

# Printing the result
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

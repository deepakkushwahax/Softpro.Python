# WAP to take input from the user and remove all the duplicates

input_string = input("Enter a string: ")
unique_string = ""
for char in input_string:
    if char not in unique_string:
        unique_string += char
print("String with duplicates removed:", unique_string)





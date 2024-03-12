
user_string = input("Enter the String: ")
new_string = ""
count = {}

for char in user_string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
        new_string += char

compressed_string = ''.join([f"{char}{count[char]}" for char in count])

print("Compressed String:", compressed_string)
print("Word Count:", len(count))


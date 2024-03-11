user_str = input("Enter the String: ")
new_str = ""
count = 1
for i in range(1, len(user_str)):
    if user_str[i]==user_str[i-1]:
        count += 1
    else:
        new_str += user_str[i-1]+str(count)
        count = 1
new_str +=user_str[-1] + str(count)
print("compressed string:",new_str)
print(type(new_str))

# WAP to take input from the user and remove all the duplicates



str1 = input("Enter a string: ")
new_str = ""
for i in str1:
    if i in new_str:
        pass
    else:
        new_str=new_str+i
print("String duplicates: ",new_str)





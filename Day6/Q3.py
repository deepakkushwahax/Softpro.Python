#take sentence as input, now count the occurence of word "The" in python without using the function
str = str(input("str user: "))
count = 0
new_str = str.split()
print(new_str)
for i in new_str:
    print(i)
    if(i == "The"):
        count = count+1
    else:
        pass
print("Total Occerrnce of The: ",count)
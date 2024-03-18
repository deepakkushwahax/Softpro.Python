# taking the list as an input from the user and remove all its duplicates using set().

new_list = input("Enter the list")
new_list = new_list.split()
new_list = list(set(new_list))
print(new_list)



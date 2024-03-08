# wap to take the name of the user and print his short name
#input::--mahesh Kumar Singh
#o/p::::-----M.K Singh

full_name = input("Enter your full name: ")
name_parts = full_name.split()
short_name = ""
for i in name_parts[:-1]:
    short_name += i[0].upper() + "."
short_name += name_parts[-1]

print("Short name:", short_name)

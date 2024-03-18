# wap to take the name of the user and print his short name
#input::--mahesh Kumar Singh
#o/p::::-----M.K Singh
#
# full_name = input("Enter your full name: ")
# name_parts = full_name.split()
# short_name = ""
# for i in name_parts[:-1]:
#     short_name = short_name+i[0].upper() + "."
# short_name = short_name+name_parts[-1]
# print("Short name:", short_name)

str = str(input("Enter the Full Names: "))
name_parts = str.split()
SN = ""
for i in name_parts[:-1]:
    SN = SN+i[0].upper()+"."
    SN = SN+name_parts[-1]
print("Short Name:", SN)











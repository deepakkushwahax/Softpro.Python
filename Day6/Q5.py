# Short Names Print

str = str(input("Enter the Full Names: "))
name_parts = str.split()
SN = ""
for i in name_parts[:-1]:
    SN = SN+i[0].upper()+"."
    SN = SN+name_parts[-1]
print("Short Name:", SN)











#max in list
list = [3,8,2,9,7,17]
current_max_number = list[0]
for i in list:
    if i>current_max_number:
        current_max_number = i

print (current_max_number)
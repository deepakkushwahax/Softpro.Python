#max in list
list = [3,8,2,9,7,17]
current_min_number = list[0]
for i in list:
    if i<current_min_number:
        current_min_number = i

print (current_min_number)
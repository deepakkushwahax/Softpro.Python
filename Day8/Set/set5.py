input_string = input("Enter elements of the list separated by commas: ")
input_list = input_string.split(',')
unique_set = set(input_list)
unique_list = list(unique_set)

print("List with duplicates removed:", unique_list)

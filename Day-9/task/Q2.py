# WAP to create a function search(), in serach function pass two parameter first, a list of ten number
# and second a number to serach . if number is present in list written index of list otherwise return false.
def search(number_list, target):

    if target in number_list:
        return number_list.index(target)
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_number = 5
result = search(numbers, search_number)
if result is not False:
    print(f"The number {search_number} is found at index {result}.")
else:
    print(f"The number {search_number} is not found in the list.")

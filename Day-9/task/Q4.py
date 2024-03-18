# WAP to create a function search(), in search function pass two parameters first,
# a list of ten numbers and second, a number to search. if number is present in list return index of list otherwise
# return false.



def search(number_list, target):
    if target in number_list:
        return number_list.index(target)
    else:
        return False

# Example usage:
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
search_number = 30
result = search(numbers, search_number)
print(result)  # Output will be the index of 30 in the list, which is 2

search_number = 55
result = search(numbers, search_number)
print(result)  # Output will be False since 55 is not in the list

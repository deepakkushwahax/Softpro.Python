# # write a program to rake name and % of marks of students in a dictionarty and display the information
#
# dic1 = {}
# n = int(input("Enter number of students: "))
# i = 1
# while i <= n:
#     name = input("Enter the Student Name")
#     marks = input("Enter % of makes of student")
#     dic1[name] = marks
#     i = i + 1
# for x in dic1:
#     print(x,dic1[x])

dic1 = {}
n = int(input("Enter number of students: "))
i = 1
while i <= n:
    name = input("Enter the Student Name: ")
    marks = input("Enter % of marks of student: ")
    dic1[name] = marks
    i = i + 1
for x in dic1:
    print(x, dic1[x])


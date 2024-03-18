def update(list):
    for i in list:
        i = i+1
        list.insert(0,i)
        print(list)
        break
new_list = [1,2,3,4]
update(new_list)
print(new_list)

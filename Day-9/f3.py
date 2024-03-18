# ---------------call by reference in python function----------
def update(ls):
    print(id(ls))
    ls[1] = 25
    print("ls",ls)

list = [10,20,30]
print(id(list))
update(list)
print("lst",list)
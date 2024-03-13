# wap to make a simple calculator using user defined functions

def cal(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y

    return a,b,c,d
x = int(input("Enter the a: "))
y = int(input("Enter the b: "))


a,b,c,d = cal(x,y)
print("Addition of a:",a)
print("Substraction of a:",b)
print("multiplication of a:",c)
print("division of a:",d)


# -----pass a list in a function and count the even and odd inside that list.-----
def count(ls):
    even = 0
    odd = 0
    for i in ls:
        if (i % 2 == 0):
            even = even+1

        else:
            odd = odd+1

    return even,odd

list = [1,2,3,4,5,6,7,8,9,10]

e,o = count(list)
print("even: ",e)
print("odd: ",o)

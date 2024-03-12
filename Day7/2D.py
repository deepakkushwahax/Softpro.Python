from numpy import *
arr = array([
    [1,2,4,5],
    [1,2,4,5]
])
print(arr)

print(arr.ndim)

print(arr.shape)

print(arr.size)

arr2 = arr.flatten()
arr3 = arr2.reshape(4,2)
print(arr3)

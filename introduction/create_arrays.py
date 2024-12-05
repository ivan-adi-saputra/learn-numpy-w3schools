import numpy as np

arr = np.array([2,6,4,7,4,3,7,3,4,6,8])
print(arr)
print(type(arr))

arr1 = np.array((1, 2, 3, 4, 5))
print(arr1)

arr2 = np.array(34)
print(arr2)

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)

# ndim digunakan untuk menghitung dimensi yang dimiliki
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim) # o
print(b.ndim) # 1
print(c.ndim) # 2
print(d.ndim) # 3

arr4 = np.array([2,4,7,2], ndmin=5)
print(arr4) # [[[[[2 4 7 2]]]]]
print(arr4.ndim) # 5
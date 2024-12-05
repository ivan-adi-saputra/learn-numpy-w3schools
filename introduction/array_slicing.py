import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# [start:end]

print(arr[1:3]) # 2 3

print(arr[2:]) #  4 5 6 7

print(arr[:3]) # 1 2 3

print(arr[-3:-1]) # 5 6

# [start:end:step]

print(arr[1:5:2]) # 2 4
# 1 - 5 = 2 3 4 5
# step 2 = 2 4  -> Meloncat 2 langkah untuk setiap elemen yang dipilih.

print(arr[::2]) # 1 3 5 7

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr1[1, 1:3]) # 7 8

print(arr1[0:3, 2]) # 3 8 -> dari kedua element, kembalikan index ke 2

print(arr1[0:2, 1:3]) # [2 3] [7 8]
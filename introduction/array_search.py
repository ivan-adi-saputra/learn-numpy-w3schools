import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

arr4 = np.where(arr == 4)
print(arr4) # (array([3, 5, 6]),) -> merepresentasikan dari index

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

arr_modulus = np.where(arr % 2 == 0)
print(arr_modulus) # (array([1, 3, 5, 6]),) -> merepresentasikan dari index

# searchsorted -> digunakan untuk mencari dimana element bisa di sisipkan (default side='left') agar bisa urut
arr_sorted = np.searchsorted(arr1, 3)
print(arr_sorted) # 2

arr_side = np.searchsorted(arr1, 3, side='right')
print(arr_side) # 3

arr2 = np.array([1, 3, 5, 7])
arr_multiple = np.searchsorted(arr, [2, 4, 6])
print(arr_multiple) # [3 7 1]







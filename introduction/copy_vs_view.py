import numpy as np

arr = np.array([1,2,3,4,5])
arr_copy = arr.copy()
arr[0] = 42
print(arr) # [42  2  3  4  5]
print(arr_copy) # [1 2 3 4 5]

arr1 = np.array([1,2,3,4,5])
arr1_view = arr1.view()
arr1[0] = 42
print(arr1) # [42  2  3  4  5]
print(arr1_view) # [42  2  3  4  5]

# definisi copy dan view, copy memiliki data tetapi view tidak memiliki data. untuk memeriksa bisa menggunakan base
# Setiap array NumPy memiliki atribut base yang mengembalikan None jika array tersebut memiliki data.
arr2 = np.array([1, 2, 3, 4, 5])
x = arr2.copy()
y = arr2.view()
print(x.base) # None -> karena memiliki data
print(y.base) # [1 2 3 4 5] -> karena tidak memiliki data
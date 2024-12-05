import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr1 = arr.reshape(4,3)
print(new_arr1)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

new_arr2 = arr.reshape(2,3,2)
print(new_arr2)
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

# cek apakah mengembalikan copy or view
check = arr.reshape(4,3).base
print(check) # [ 1  2  3  4  5  6  7  8  9 10 11 12]

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr3 = arr1.reshape(2,2,-1) # ketika menggunakan minus maka akan menghitung otomatis dimensi tersebut
print(new_arr3)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
new_arr4 = arr2.reshape(-1) # mengubah jadi 1 dimensi
print(new_arr4)
# [1 2 3 4 5 6]

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr_join = np.concatenate((arr1, arr2))
print(arr_join)
# [1 2 3 4 5 6]

# axis=1 -> join array 2D 
# Axis 0: Sepanjang baris (dimensi pertama). Operasi dilakukan per kolom.
# Axis 1: Sepanjang kolom (dimensi kedua). Operasi dilakukan per baris.
# Axis N: Dimensi lebih tinggi pada array multidimensi.
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr_axis_join = np.concatenate((arr3, arr4), axis=1)
print(arr_axis_join)
# [[1 2 5 6]
#  [3 4 7 8]]

arr_stack_join = np.stack((arr1,arr2), axis=1)
print(arr_stack_join)
# [[1 4]
#  [2 5]
#  [3 6]]

hstack = np.hstack((arr1,arr2)) # sepanjang baris
print(hstack) # [1 2 3 4 5 6]

vstack = np.vstack((arr1,arr2)) # sepanjang column
print(vstack)
# [[1 2 3]
#  [4 5 6]]

dstack = np.dstack((arr1,arr2)) # sepanjang tinggi, yang sama dengan kedalaman
print(dstack) # menghasilkan dimensi baru
# [[[1 4]
#   [2 5]
#   [3 6]]]

# concatenate -> tidak menambahkan dimensi baru
# stack -> menambahkan dimensi baru



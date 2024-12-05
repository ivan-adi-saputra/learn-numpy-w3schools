import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
arr_split = np.array_split(arr, 3)
print(arr_split) # [array([1, 2]), array([3, 4]), array([5, 6])]

print(arr_split[0]) # [1 2]
print(arr_split[1]) # [3 4]
print(arr_split[2]) # [5 6]

arr_split1 = np.array_split(arr, 4)
print(arr_split1) # [array([1, 2]), array([3, 4]), array([5]), array([6])]

arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr1_split = np.array_split(arr1, 3)
print(arr1_split)
# [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#        [7, 8]]), array([[ 9, 10],
#        [11, 12]])]

arr1_axis = np.array_split(arr1, 2, axis=1)
print(arr1_axis)
# [array([[ 1],
#        [ 3],
#        [ 5],
#        [ 7],
#        [ 9],
#        [11]]), array([[ 2],
#        [ 4],
#        [ 6],
#        [ 8],
#        [10],
#        [12]])]

arr1_hsplit = np.hsplit(arr1, 2) # sepanjang baris
print(arr1_hsplit)
# [array([[ 1],
#        [ 3],
#        [ 5],
#        [ 7],
#        [ 9],
#        [11]]), array([[ 2],
#        [ 4],
#        [ 6],
#        [ 8],
#        [10],
#        [12]])]



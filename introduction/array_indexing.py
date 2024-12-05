import numpy as np

arr = np.array([1,6,2])
print(arr[0]) # 1

arr1 = np.array([[4,6,3], [8,7,4]])
print(arr1[0,1]) # 6

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2[1,0,2]) # 9

# Negative Indexing
print(arr2[0,1,-1]) # 6
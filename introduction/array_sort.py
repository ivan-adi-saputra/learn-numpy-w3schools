import numpy as np

arr = np.array([3, 2, 0, 1])

arr_short = np.sort(arr)
print(arr_short) # [0 1 2 3]

arr_string = np.array(['banana', 'cherry', 'apple'])
arr_string_sort = np.sort(arr_string)
print(arr_string_sort) # ['apple' 'banana' 'cherry']

arr_bool = np.array([True, False, True])
arr_bool_sort = np.sort(arr_bool)
print(arr_bool_sort) # [False  True  True]

arr_2d = np.array([[3, 2, 4], [5, 0, 1]])
arr_2d_sort = np.sort(arr_2d)
print(arr_2d_sort)
# [[2 3 4]
#  [0 1 5]]


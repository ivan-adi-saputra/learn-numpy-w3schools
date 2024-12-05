import numpy as np

arr_numbers = np.array([1,2,3,4])
print(arr_numbers.dtype) # int64

arr_strings = np.array(['apple', 'banana', 'cherry'])
print(arr_strings.dtype) # <U6

arr1 = np.array([1,2,3,4,5], dtype='S')
print(arr1) # [b'1' b'2' b'3' b'4' b'5']
print(arr1.dtype) # |S1

arr2 = np.array([1, 2, 3, 4], dtype='i4')
print(arr2) # [1 2 3 4]
print(arr2.dtype) # int32

arr3 = np.array([1, 2, 3, 4], dtype='i')
print(arr3) # [1 2 3 4]
print(arr3.dtype) # int32

# mengubah data float ke integer
arr_float = np.array([1.2, 2.3, 3.4, 4.5, 5.6])
new_arr_integer = arr_float.astype('i') # parameter 'i' / int
print(new_arr_integer) # [1 2 3 4 5]
print(new_arr_integer.dtype) # int32

arr_integer = np.array([1,0,3])
new_arr_bool = arr_integer.astype(bool)
print(new_arr_bool) # [ True False  True]
print(new_arr_bool.dtype) # bool


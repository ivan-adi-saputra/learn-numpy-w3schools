import numpy as np

arr = np.array([41, 42, 43, 44])
b = [True, False, True, False]

new_arr = arr[b]
print(new_arr) # [41 43]

more_than_condition = arr > 42
new_arr_more_than = arr[more_than_condition]
print(more_than_condition) # [False False  True  True]
















import numpy as np 

arr = np.array([1,2,3])

for x in arr:
    print(x)
# 1
# 2
# 3

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr1:
    print(x)
# [1 2 3]
# [4 5 6]

for x in arr1:
  for y in x:
    print(y)
# 1
# 2
# 3
# 4
# 5
# 6

arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr2):
   print(x)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# op_dtypes -> mengubah type data (yang ditentukan) selama iterasi
# buffer -> spasi exstra agar bisa di ubah type data
# flags=['buffered'] -> untuk mengaktifkannya dalam nditer()
for x in np.nditer(arr2, flags=['buffered'], op_dtypes='S'):
   print(x)
# np.bytes_(b'1')
# np.bytes_(b'2')
# np.bytes_(b'3')
# np.bytes_(b'4')
# np.bytes_(b'5')
# np.bytes_(b'6')
# np.bytes_(b'7')
# np.bytes_(b'8')

# untuk skip 1 element -> mengacu pada dimensi
for x in np.nditer(arr2[:, ::2]):
   print(x)
# 1
# 2
# 5
# 6

for index, value in np.ndenumerate(arr2):
   print(f'index: {index}, value: {value}')
# index: (0, 0, 0), value: 1
# index: (0, 0, 1), value: 2
# index: (0, 1, 0), value: 3
# index: (0, 1, 1), value: 4
# index: (1, 0, 0), value: 5
# index: (1, 0, 1), value: 6
# index: (1, 1, 0), value: 7
# index: (1, 1, 1), value: 8








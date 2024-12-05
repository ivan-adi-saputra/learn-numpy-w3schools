import numpy as np

# Array NumPy memiliki atribut bernama shape yang mengembalikan tuple dengan setiap indeks memiliki jumlah elemen yang sesuai.
# mengembalikan tuple
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# membuat array NumPy 2D
print(arr.shape) # (2, 4) -> 2 = Jumlah baris (dimensi pertama), 4 =  Jumlah kolom (dimensi kedua)

arr1 = np.array([1,2,3,4], ndmin=5)
print(arr1)
print(arr1.shape)



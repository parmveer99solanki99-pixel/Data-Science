# sort   

import numpy as np

# 1d array
# arr = np.array([10, 40, 30, 60, 50, 7, 5])
# print(arr)

# arr_s = np.sort(arr)
# print(arr_s)

# 2d

# arr1 = np.array([[5, 60, 20],[40, 90, 4]])
# print(arr1)

# arr1_s = np.sort(arr1, axis = 0)
# print(arr1_s) 


# by default sorting -> ascending || deascending

# arr = np.array([[5, 36, 4, 12, 8], [33, 3, 67, 22, 34]])
# print(arr)

# ascending order

# arr_s = np.sort(arr)
# print(arr_s)

# descending order

# arr_ds = np.sort(arr)[:, :: -1]
# print(arr_ds)




# filter

# arr = np.array([10, 20, 40, 6, 3, 4, 2])
# print(arr)
# arr_f = arr[arr < 40]
# print(arr_f)


# example


# arr = np.array([10, 20, 40, 6, 3, 4, 2])
# print(arr)
# arr_f = arr[arr % 2 == 0]
# print(arr_f)


# Fancy Indexing

# arr = np.array([10, 20, 3, 4, 90, 100])
# print(arr)
# arr_f = arr[[0, 2, 5]]
# print(arr_f)



# np.where

# 1d

# arr = np.array([10, 3, 4, 80, 90, 100])
# print(arr)
# arr_w = np.where(arr < 40, "True", "False")
# print(arr_w)


# arr = np.array([10, 3, 4, 80, 90, 100])
# print(arr)
# arr_w = np.where(arr > 40, arr + 2, arr - 2)
# print(arr_w)





# Adding & Removing

# concatenate

# arr1 = np.array([10, 20, 30])
# arr2 = np.array([1, 2, 3])

# concatenate method
# arr1_arr2 = np.concatenate((arr1, arr2))
# print(arr1_arr2)

# manually

# arr1_arr2_new = arr1 + arr2
# print(arr1_arr2_new)


# 2d


# arr1 = np.array([[10, 20, 30], [40, 50, 60]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1)
# print(arr2)

# arr1_arr2 = np.concatenate((arr1, arr2))
# print(arr1_arr2)



# Statistical Functions

# arr = np.array([10, 20, 30])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.median(arr))
# print(np.min(arr))
# print(np.max(arr))


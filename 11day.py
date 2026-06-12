# Array Reshaping

# reshape array

import numpy as np

# arr = np.arange(12)   # 12 -> 3*4 || 12-> 4*3
# up_arr = np.reshape(arr, (3,4))
# print(up_arr)  


# example

# arr1 = np.arange(24)
# up_arr1 = np.reshape(arr1, (3, 2, 4))
# print(up_arr1)


# flatten

# arr = np.arange(12).reshape(3, 4)
# print(arr)
# up_arr = arr.flatten()
# print(up_arr)


# example 3d

arr = np.arange(24).reshape(2, 3, 4)
print(arr)
up_arr = arr.flatten()
print(up_arr)



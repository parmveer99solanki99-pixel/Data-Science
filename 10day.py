# list

# l = [1, 2, 3]
# print(l)

# array 1d 

import numpy as np

# arr = np.array([1, 2, 3])
# print(arr)


# array 2d

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)


# example
# 2d array

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# print(arr[0])
# print(arr[0][0])


# example array value 4 -> 100

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# arr[1][0] = 100
# print(arr)

# list

# l = [1, 2, 3]
# lm = l*2
# print(lm)

#array

# arr = np.array(l)
# arrM = arr*2
# print(arrM)

# comparison
# list

# import time
# start = time.time()
# l = [i*2 for i in range(1000000)]
# print("list output:", time.time() - start)


# array

# start = time.time()
# arr = np.array(1000000) * 2
# print("array output:", time.time() - start)


# zeros array 1d

# arr = np.zeros(5)
# print(arr)

# zeros array 2d

# arr1 = np.zeros((2,3))
# print(arr1)


# ones array 1d

# arr = np.ones(5)
# print(arr)


# ones array 2d

# arr1 = np.ones((2,3))
# print(arr1)


# zeros & ones array 2d

# arr = np.zeros((2,3)) + 10
# print(arr)
# arr = np.ones((2,3)) + 5
# print(arr)


# full array 1d

# arr = np.full((3), 5)
# print(arr)


# full array 2d

# arr = np.full((2,3), 5)
# print(arr)


# arr = np.zeros((2,3)) + 6
# print(arr)

# arr = np.full((2,3), 1)
# print(arr)

# arange for 1d

# arr = np.arange(5)
# print(arr)

# # arange for 2d

# arr1 = np.arange(2,3)
# print(arr1)


# vector 1d list
# l = [1, 2, 3]
# print(l)

# vector 1d array
# arr = np.array(l)
# print(arr)


# matrix 2d list
# l = [[1,2,3], [4, 5, 6]]
# print(l)

# matrix 2d array
# arr = np.array(l)
# print(arr)


# tensor 3d list
# l = [[1,2], [3, 4], [5,6], [7, 8]]
# print(l)

# tensor 3d array
# arr = np.array(l)
# print(arr)



# array

arr = np.arange(11)
print("Shape:",arr.shape)
print("Shape:",np.shape(arr))
print("Dimension:",np.ndim(arr))
print("Size:",np.size(arr))
print("Datatype:",arr.dtype)

import numpy as np

# For a 1D array
a = np.array([1, 2, 3, 4])
print(a)

# For a 2D array (matrix)
b = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
print(b)


# For a 3D array (cube)

c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c)


# get the dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(a.shape)
print(b.shape)
print(c.shape)
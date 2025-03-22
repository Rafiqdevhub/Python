import numpy as np

# Create a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
# print("1D Array:", arr_1d)

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print("2D Array:\n", arr_2d)

# Create a 3D array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
dimension = arr_3d.ndim
# print("Number of dimensions:", dimension)
# print("3D Array:\n", arr_3d)


heights = np.random.randint(150, 200, size=100000)

# Calculating the average height
average_height = np.mean(heights)
print("Average Height:", average_height)
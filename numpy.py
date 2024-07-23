import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
print("Array 1:", array1)

array2 = np.linspace(0, 10, 5)
print("Array 2:", array2)

array3 = np.zeros((2, 3))
print("Array 3:", array3)

array4 = np.ones((2, 3))
print("Array 4:", array4)

array5 = np.arange(0, 10, 2)
print("Array 5:", array5)

reshaped_array = np.reshape(array1, (5, 1))
print("Reshaped Array 1:", reshaped_array)

mean_value = np.mean(array1)
print("Mean of Array 1:", mean_value)

median_value = np.median(array1)
print("Median of Array 1:", median_value)

std_deviation = np.std(array1)
print("Standard Deviation of Array 1:", std_deviation)

sum_value = np.sum(array1)
print("Sum of Array 1:", sum_value)

prod_value = np.prod(array1)
print("Product of Array 1:", prod_value)

array6 = np.array([6, 7, 8, 9, 10])
dot_product = np.dot(array1, array6)
print("Dot Product of Array 1 and Array 6:", dot_product)

multi_dim_array = np.array([[1, 2, 3], [4, 5, 6]])
transposed_array = np.transpose(multi_dim_array)
print("Transposed Multi Dimensional Array:", transposed_array)

min_value = np.min(array1)
print("Minimum of Array 1:", min_value)

max_value = np.max(array1)
print("Maximum of Array 1:", max_value)

concatenated_array = np.concatenate((array1, array6))
print("Concatenated Array:", concatenated_array)

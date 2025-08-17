import numpy as np

# ---------------------------------------
# --TASK-1
# Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("Original List:", original_list)
print("One-dimensional NumPy array:", array_1d)

# ---------------------------------------
# --TASK-2
# Create 3x3 Matrix (2–10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
matrix = np.arange(2, 11).reshape(3, 3)
print("\n3x3 Matrix from 2 to 10:\n", matrix)

# ---------------------------------------
# --TASK-3
# Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
null_vector = np.zeros(10)
print("\nNull Vector:", null_vector)
null_vector[5] = 11
print("Updated Null Vector:", null_vector)

# ---------------------------------------
# --TASK-4
# Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.
array_range = np.arange(12, 38)
print("\nArray from 12 to 38:", array_range)

# ---------------------------------------
# --TASK-5
# Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.
arr = np.array([1, 2, 3, 4])
arr_float = arr.astype(float)
print("\nOriginal array:", arr)
print("Converted to float:", arr_float)

# ---------------------------------------
# --TASK-6
# Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees.
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32
print("\nValues in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# ---------------------------------------
# --TASK-7
# Append Values to Array
# Write a NumPy program to append values to the end of an array.
arr2 = np.array([10, 20, 30])
arr_appended = np.append(arr2, [40, 50, 60, 70, 80, 90])
print("\nOriginal array:", arr2)
print("After append:", arr_appended)

# ---------------------------------------
# --TASK-8
# Array Statistical Functions
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation.
random_arr = np.random.randint(1, 100, 10)
print("\nRandom Array:", random_arr)
print("Mean:", np.mean(random_arr))
print("Median:", np.median(random_arr))
print("Standard Deviation:", np.std(random_arr))

# ---------------------------------------
# --TASK-9
# Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.
random_matrix = np.random.rand(10, 10)
print("\n10x10 Random Matrix:\n", random_matrix)
print("Min value:", random_matrix.min())
print("Max value:", random_matrix.max())

# ---------------------------------------
# --TASK-10
# 3x3x3 Random Array
# Create a 3x3x3 array with random values.
random_3d = np.random.rand(3, 3, 3)
print("\n3x3x3 Random Array:\n", random_3d)

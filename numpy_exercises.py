import numpy as np

# #Use the following code for the questions below:
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

neg_nums = np.count_nonzero(a < 0)
print(neg_nums)

# How many positive numbers are there?

pos_nums = np.count_nonzero(a > 0)
print(pos_nums)

# How many even positive numbers are there?

even_pos_nums = np.count_nonzero((a > 0) & (a % 2 == 0))
print(even_pos_nums)

# If you were to add 3 to each data point, how many positive numbers would there be?

a_plus_three = a + 3
plus_three_pos = np.count_nonzero(a_plus_three > 0)
print(plus_three_pos)

# If you squared each number, what would the new mean and standard deviation be?

a_squared = a ** 2
squared_mean = np.mean(a_squared)
squared_std = np.std(a_squared)
print(squared_mean)
print(squared_std)

# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(np.mean(a))
print(a - (np.mean(a)))
print(np.sort(a))

# Calculate the z-score for each data point. Recall that the z-score is given by:

a_std = np.std(a)
a_mean = np.mean(a)
print(a_std)
print(a_mean)
a_zscores = ((a - a_mean)/a_std)
print(a_zscores)

# Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.



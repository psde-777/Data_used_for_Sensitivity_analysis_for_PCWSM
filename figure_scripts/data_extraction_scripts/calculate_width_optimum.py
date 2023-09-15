import numpy as np

# Read data from files
output_file = 'output_values_trial_run.txt'
param_file = 'param_values_trial_run.txt'

output_values = np.loadtxt(output_file)
param_values = np.loadtxt(param_file)

# Extract the second to last column from param_values
x_values = param_values[:, -2]

# Filter data points where y < 75
filtered_indices = np.where(output_values < 75)[0]
filtered_x_values = x_values[filtered_indices]
filtered_output_values = output_values[filtered_indices]

# Sort filtered_x_values and find the indices for 5% quantiles
sorted_indices = np.argsort(filtered_x_values)
num_points = len(sorted_indices)
left_index = sorted_indices[int(0.01 * num_points)]
right_index = sorted_indices[int(0.99 * num_points)]

# Find the data points at the 5% quantiles
left_data_point = (filtered_x_values[left_index], filtered_output_values[left_index])
right_data_point = (filtered_x_values[right_index], filtered_output_values[right_index])

print("Data point where 5% of points below 75 lie to the left:")
print("x:", left_data_point[0], "y:", left_data_point[1])

print("Data point where 5% of points below 75 lie to the right:")
print("x:", right_data_point[0], "y:", right_data_point[1])


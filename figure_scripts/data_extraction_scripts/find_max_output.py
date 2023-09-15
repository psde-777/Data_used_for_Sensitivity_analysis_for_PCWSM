import numpy as np

# Load data from text file
data = np.loadtxt('output_values_trial_run.txt')

# Determine the number of values to find (0.5% of total values)
num_values = int(len(data) * 0.001)

# Find the indices of the lowest values
indices = np.argsort(data)[-num_values:]

# Print the indices of the lowest values
print("Indices of the highest values:", indices)
np.savetxt("highest_output_indices.txt", indices)



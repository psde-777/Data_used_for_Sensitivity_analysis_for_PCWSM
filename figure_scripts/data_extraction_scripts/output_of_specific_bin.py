import numpy as np
import matplotlib.pyplot as plt

param_values = np.loadtxt('param_values_trial_run.txt')
output_values = np.loadtxt('output_values_trial_run.txt')
column = 0
maximum_value = 1000

indices = np.where(param_values[:, column] < maximum_value)[0]

EG_values = param_values[indices, column]
var_values_EG = output_values[indices]

np.savetxt("EG_values.txt", EG_values)
np.savetxt("var_values_EG.txt", var_values_EG)

print(indices.shape)
print(EG_values.shape)
print(var_values_EG.shape)
#print(indices[0])
#print(CBH_values[0])
#print(var_values[0])
#print(indices[62000])
#print(CBH_values[62000])
#print(var_values[62000])

#num_values = 100
#ind = np.argsort(var_values)[-num_values:]
#print(ind)
#print(CBH_values[ind])
#print(var_values[ind])

from numpy import full,savetxt
import sys
import numpy as np
import sys
#argv[1] = sample size
#argv[2] = parameter size
#argv[3] = parameter sets size

#initializing variables
sample_size = sys.argv[1]
parameter_size = sys.argv[2]
N = sys.argv[3]

print(N)
var = np.zeros((N))
print(var.shape)

#setting output data
with open("output_values_trial_run.txt","w") as f:
    for i in range(N):
        print(i)
        var[i] = np.loadtxt("family_1/Generation_1/Run_" + str(i+1) + "/Output/var_high.txt")
        f.write(str(var[i]) + "\n")
        #print(str(var[i]))

f.close()

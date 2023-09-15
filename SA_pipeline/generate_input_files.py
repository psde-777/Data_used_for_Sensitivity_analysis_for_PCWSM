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
parameters = np.zeros((N,parameter_size))
count = 0
count_init = 0

#loading parameter data
kin_parameters = np.loadtxt("kinetic_parameters.txt")
init_parameters = np.loadtxt("initial_configuration_parameters_high.txt")
variation_bools_kin = np.loadtxt("kin_params_to_randomize.txt",dtype = int)
variation_bools_init = np.loadtxt("init_params_to_randomize.txt",dtype = int)
parameters = np.loadtxt("param_values_trial_run.txt")
N_kin_vals = kin_parameters.size
N_init_vals = init_parameters.size


#sanity checks
print(parameters.shape)
#print(parameters[0][16])
#print(parameters[1][0])
print(N_kin_vals)
print(N_init_vals)
#N_kin_vals_2 = variation_bools_kin.size
#N_init_vals_2 = variation_bools_init.size
#print(N_kin_vals_2)
#print(N_init_vals_2)


for i in range(N):
    count = 0
    count_init = 0
    print(i)
    with open("family_1"  + "/Generation_1"  + "/Run_" + str(i+1) + "/Params/kinetic_parameters.txt","w") as f:
        for k in range(N_kin_vals):
#            print("k= " + str(k))
            if variation_bools_kin[k] == 1:
                #                print("bool=1 : sampled par = " + str(parameters[i][k-count]));
                f.write(str(parameters[i][k-count]) + "\t")
            else:
#                print("bool=0 : old par = " + str(kin_parameters[k]));
                f.write(str(kin_parameters[k]) + "\t")
                count += 1

    with open("family_1"  + "/Generation_1"  + "/Run_" + str(i+1) + "/Params/initial_configuration_parameters_high.txt","w") as f:

        for j in range(6):
#            print("j= " + str(j))
            if variation_bools_init[j] == 1:
#                print("bool=1 : sampled par = " + str(int(parameters[i][N_kin_vals-count + j-count_init])));
                f.write(str(int(parameters[i][N_kin_vals-count + j-count_init])) + "\t")
            else:
#                print("bool=0 : old par = " + str(int(init_parameters[j])));
                f.write(str(int(init_parameters[j])) + "\t")
                count_init += 1

        for j in range(6,13):
#            print("j= " + str(j))
            if variation_bools_init[j] == 1:
#                print("bool=1 : sampled par = " + str(parameters[i][N_kin_vals-count + j-count_init]));
                f.write(str(parameters[i][N_kin_vals-count + j-count_init]) + "\t")
            else:
#                print("bool=0 : old par = " + str(init_parameters[j]));
                f.write(str(init_parameters[j]) + "\t")
                count_init += 1

        for j in range(13,14):
#            print("j= " + str(j))
            if variation_bools_init[j] == 1:
#                print("bool=1 : sampled par = " + str(int(parameters[i][N_kin_vals-count + j-count_init])));
                f.write(str(int(parameters[i][N_kin_vals-count + j-count_init])) + "\t")
            else:
#                print("bool=0 : old par = " + str(int(init_parameters[j])));
                f.write(str(int(init_parameters[j])) + "\t")
                count_init += 1

        for j in range(14,N_init_vals):
#            print("j= " + str(j))
            if variation_bools_init[j] == 1:
#                print("bool=1 : sampled par = " + str(parameters[i][N_kin_vals-count + j-count_init]));
                f.write(str(parameters[i][N_kin_vals-count + j-count_init]) + "\t")
            else:
#                print("bool=0 : old par = " + str(init_parameters[j]));
                f.write(str(init_parameters[j]) + "\t")
                count_init += 1           

            


            

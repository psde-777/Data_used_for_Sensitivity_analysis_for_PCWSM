from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

# Define the model inputs
problem = {
'num_vars': 19,
'names': ['EG_rxn_rate', 'CBH_rxn_rate', 'BGL_rxn_rate', 'XYL_rxn_rate', 
        'Lignin_adhesion_rate', 'CBH_attachment_rate',
        'binding_affinity_cellobiose_to_EG', 'binding_affinity_cellobiose_to_CBH', 
        'binding_affinity_glucose_to_EG', 'binding_affinity_glucose_to_CBH', 'binding_affinity_glucose_to_BGL',
        'digestibility_ratio_cellulose', 'digestibility_ratio_hemicellulose',
        'init_EG', 'init_CBH', 'init_BGL', 'init_XYL',
        'pct_crystalline_cellu', 'pct_crystalline_hemi'],
'bounds': [[1, 10000], [1, 1000], [1, 10000], [0.001, 1],
           [100, 250], [0.0001, 1000],
           [0.01, 1], [0.01, 1],
           [0.01, 1], [0.01, 1], [0.01, 1],
           [0.00001, 0.05], [0.00001, 0.1],
           [10, 30], [20, 80], [7, 23], [20, 100],
           [0, 1], [0, 1]]
}

#Generate samples
param_values = saltelli.sample(problem, 1024, calc_second_order=False)
np.savetxt("param_values_trial_run.txt", param_values)

print(param_values.shape)

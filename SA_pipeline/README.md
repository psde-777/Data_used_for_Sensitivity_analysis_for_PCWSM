# README SA_pipeline
## Setup of the directory and data to be analysed
- Create a directory in which you want to run the analysis (this will be referred to as topdir) and copy the content of this directory into topdir
- Open topdir/latest/, and run compile.sh via the terminal command
- Check that the "Params" directory, and the "Output" directory exist within the directory "latest"
- Create a directory called "family_1" in topdir and a directory called "Generation 1“. If the directory already exists, make sure that it is empty

## Setup of experimental data

- Within topdir, there is a file "keywords.txt" (if not, you need to create it). From this file the algorithm takes the names of the experimental data sets, and the initial configuration parameters. The file needs to have two keywords, from which the first one will be used for the sensitivity analysis
- In the Output directory of “latest“, create a directory "expe_data" if it does not exist yet. Within this directory, the data to be used for the fitting procedure needs to be placed. These data need to be contained in .txt files, in which the first column is time and the second column is the sugar release percentage. If you have data for glucose and xylose, these need to be contained in separate files. The end of the file name specifies whether it is a glucose or xylose data file, i.e. expe_saccharification_keyword_glc.txt or expe_saccharification_keyword_xyl_.txt.
- You need to have one experimental data file (either for glucose or xylose) for each keyword in keywords.txt.
- Make sure that for each keyword there exists a file "initial_configuration_parameters_keyword.txt" in topdir
- Open the files “generate_input_files.py“, “evo_run.sh“, and “generate_input_file.py“ within topdir and change every instance of the word „high“ with the first keyword of your keywords

## Setup of the sensitivity analysis

- Open the files "kin_params_to_randomize.txt" and "init_params_to_randomize.txt". Here, you can choose, which parameters should be used for the analysis by setting the respective value to 0 or 1
- Open the file “generate_samples.py“. Here you need to define the number of parameters D you want to apply the sensitivity analysis on, their names, and the ranges in which you want to sample their values. You also define a sample size n in the function “saltelli.sample“. The default value is  n =1024. This value must be a power of 2. 
- You can set calc_second_order to True (the Total Sobol indices, the first Sobol indices, and the second Sobol indices will be calculated) or to False (the Total Sobol indices and the first Sobol indices will be calculated). 
- Open the file “calc_indices.py“ and copy the parameter names and ranges from “generate_samples.py“

##Running the sensitivity analysis

The sample function creates N parameter sets with N = n*(D+2). D is the number of parameters and n is the sample size. The keyword argument calc_second_order=True will not exclude second order indieces, resulting in a larger sample matrix with N = n*(2D+2) parameter sets instead. These parameters will be used as command line arguments as well as the number of cores you have available (N_cores).
Now, to start the algorithm, execute the shell script "evo_all.sh" via the following command:#

  ./evo_all.sh n D N N_cores 1>log.out 2>log.err


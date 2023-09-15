# $1 = sample size n
# $2 = parameter size D
# $3 = parameter set size N
# $4 = Maximum number of cores available


python3 generate_samples.py
bash create_folders.sh $3
python3 generate_input_files.py $1 $2 $3
bash evo_run.sh 1 1 $3 $4
bash evo_average_fit_and_print_variance.sh 1 1 $3 $4
python3 generate_output_file.py $1 $2 $3
python3 calc_indices.py


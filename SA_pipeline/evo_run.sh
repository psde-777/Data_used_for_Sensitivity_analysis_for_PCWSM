# $1 = family
# $2 = Generation number
# $3 = Number of simus in generation
# $4 = Maximum number of cores available
COUNT=1
PIDCOUNT=1
echo "Running code";
for i in $(seq 1 $3)
do
	cd family_$1/Generation_$2/Run_${COUNT}
		./code_4 high 1>run_${COUNT}.out 2>run_${COUNT}.err &
		pids[${PIDCOUNT}]=$!	
		PIDCOUNT=$((${PIDCOUNT} + 1));
		
		joblist=($(jobs -p))



		while [ ${#joblist[*]} -ge $4 ]
		do
			sleep 0.1
			joblist=($(jobs -p))
		done

	cd ../../../
	let COUNT++
done

for pid in ${pids[*]}; do
    wait $pid
done
echo "Done running code";
wait $PROCESSID



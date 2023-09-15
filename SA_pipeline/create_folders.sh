#$1 : number of Runs

for j in $(seq 1 $1)
do
	mkdir family_1/Generation_1/Run_${j}
	cp code_4 family_1/Generation_1/Run_${j}/
	cp -a latest/Output/ family_1/Generation_1/Run_${j}/
	cp -a latest/Params/ family_1/Generation_1/Run_${j}/
done


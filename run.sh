#!/bin/bash

if [ $1 -eq 1 ] 
then
    d="./Q1/"
	if [ $2 -eq 1 ]
	then
		processed=$3"p" 
		python3 "$d"process.py $3 $processed
		python3 "$d"predict.py "$d""learned_p.txt" $processed $4
	elif [ $2 -eq 2 ]
	then
		stemmed=$3"st"
		python3 "$d"stopword_stem.py $3	$stemmed
		processed=$stemmed"p" 
		python3 "$d"process.py $stemmed $processed
		
		python3 "$d"predict.py "$d""learned_st_p.txt" $processed $4 
	elif [ $2 -eq 3 ]
	then
		stemmed=$3"st"
		python3 "$d"stopword_stem.py $3	$stemmed
		processed=$stemmed"p1" 
		python3 "$d"process_e_1.py $stemmed $processed

		python3 "$d"predict.py "$d""learned_st_p1.txt" $processed $4
	elif [ $2 -eq 4 ]
	then
		stemmed=$3"st"
		python3 "$d"stopword_stem.py $3	$stemmed
		processed=$stemmed"p2" 
		python3 "$d"process_e_2.py $stemmed $processed

		python3 "$d"predict.py "$d""learned_st_p2.txt" $processed $4
	elif [ $2 -eq 5 ]
	then
		stemmed=$3"st"
		python3 "$d"stopword_stem.py $3	$stemmed
		processed=$stemmed"p3" 
		python3 "$d"process_e_3.py $stemmed $processed

		python3 "$d"predict.py "$d""learned_st_p3.txt" $processed $4
	else
		echo "Invalid arguments"
	fi	
	
elif [ $1 -eq 2 ]
then
	d="./Q2/"
	if [ $2 -eq 1 ]
	then
		python3 "$d"q2predict.py "$d""pegasos.txt" $3 $4
	elif [ $2 -eq 2 ]
	then
		python3 "$d"q2_cpredict.py $3 $4
	elif [ $2 -eq 3 ]
	then
		python3 "$d"q2_dpredict.py $3 $4
	else
		echo "Invalid arguments"
	fi	
else 
     	echo "Unknown option"
fi
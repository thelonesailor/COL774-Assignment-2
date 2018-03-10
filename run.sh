#!/bin/bash

if [ $1 -eq 1 ] 
then
    d="./Q1/"
	if [ $2 -eq 1 ]
	then
		python3 "$d"predict.py "$d""learned_p.txt" $3 $4 1
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
		processed=$stemmed"p" 
		python3 "$d"process.py $stemmed $processed

		python3 "$d"predict.py "$d""learned_st_p1.txt" $processed $4 1
	else
		echo "Invalid arguments"
	fi	
	
# elif [ $1 -eq 2 ]
# then
#     cd Q2
# 	if [$2 -eq 1]
# 	then

# 	elif [$2 -eq 2]
# 	then

# 	elif [$2 -eq 3]
# 	then

# 	else
# 		echo "Invalid arguments"
# 	fi	
# 	cd..
else 
     	echo Unknown option.
fi
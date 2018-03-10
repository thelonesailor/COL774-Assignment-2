#!/bin/bash
# echo "Train data"
# ./run.sh 1 1 "./Q1/imdb/imdb_train_text_p.txt" "predictions"
# python3 checkq1.py 1 "predictions" "./Q1/imdb/imdb_train_labels.txt" "./Q1/learned_p.txt"
# echo "----------------------------------"
# echo "Test data"
# ./run.sh 1 1 "./Q1/imdb/imdb_test_text_p.txt" "predictions"
# python3 checkq1.py 1 "predictions" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_p.txt"
# echo "----------------------------------"

echo "Test data"
./run.sh 1 2 "./Q1/imdb/imdb_test_text.txt" "temp"
python3 checkq1.py 2 "temp" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_st_p.txt"
echo "------------------------------------"

echo "Test data"
./run.sh 1 3 "./Q1/imdb/imdb_test_text.txt" "temp"
python3 checkq1.py 3 "temp" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_st_p1.txt"
echo "------------------------------------"

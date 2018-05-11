#!/bin/bash
# echo "Train data"
# ./run.sh 1 1 "./Q1/imdb/imdb_train_text.txt" "temp"
# python3 checkq1.py 1 "temp" "./Q1/imdb/imdb_train_labels.txt" "./Q1/learned_p.txt"
# echo "----------------------------------"
# echo "Test data"
# ./run.sh 1 1 "./Q1/imdb/imdb_test_text.txt" "temp"
# python3 checkq1.py 1 "temp" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_p.txt"
# echo "----------------------------------"

echo "Test data"
./run.sh 1 2 "./Q1/imdb/imdb_test_text.txt" "temp"
python3 checkq1.py 2 "temp" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_st_p.txt"
echo "------------------------------------"

# echo "Test data"
# ./run.sh 1 3 "./Q1/imdb/imdb_test_text.txt" "temp"
# python3 checkq1.py 3 "temp" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_st_p1.txt"
# echo "------------------------------------"

# echo "Test data"
# ./run.sh 1 4 "./Q1/imdb/imdb_test_text.txt" "temp"
# python3 checkq1.py 4 "temp" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_st_p2.txt"
# echo "------------------------------------"

# echo "Test data"
# ./run.sh 1 5 "./Q1/imdb/imdb_test_text.txt" "temp"
# python3 checkq1.py 5 "temp" "./Q1/imdb/imdb_test_labels.txt" "./Q1/learned_st_p3.txt"
# echo "------------------------------------"


# echo "Train data"
# ./run.sh 2 1 "./Q2/train_image.csv" "temp"
# python3 checkq2.py 1 "temp" "./Q2/train_label.csv"
# echo "------------------------------------"
# echo "Test data"
# ./run.sh 2 1 "./Q2/test_image.csv" "temp"
# python3 checkq2.py 1 "temp" "./Q2/test_label.csv"
# echo "------------------------------------"

# echo "Test data"
# ./run.sh 2 2 "./Q2/test_image.csv" "temp"
# python3 checkq2.py 2 "temp" "./Q2/test_label.csv"
# echo "------------------------------------"

# echo "Test data"
# ./run.sh 2 3 "./Q2/test_image.csv" "temp"
# python3 checkq2.py 3 "temp" "./Q2/test_label.csv"
# echo "------------------------------------"

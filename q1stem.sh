#!/bin/bash
cd Q1

python3 stopword_stem.py "./imdb/imdb_train_text.txt" "./imdb/imdb_train_text_st.txt"
python3 stopword_stem.py "./imdb/imdb_test_text.txt" "./imdb/imdb_test_text_st.txt"

cd ..
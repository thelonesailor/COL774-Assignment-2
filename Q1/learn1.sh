# #!/bin/bash
python3 stopword_stem.py "./imdb/imdb_test_text.txt" "./imdb/imdb_test_text.txtst"
python3 stopword_stem.py "./imdb/imdb_train_text.txt" "./imdb/imdb_train_text.txtst"
echo "stemming done"

python3 process.py "./imdb/imdb_train_text.txt" "./imdb/imdb_train_text.txtp"
python3 process.py "./imdb/imdb_test_text.txt" "./imdb/imdb_test_text.txtp"  
python3 train.py "./imdb/imdb_train_text.txtp" "./imdb/imdb_train_labels.txt" "learned_p.txt"
echo "p done"

python3 process.py "./imdb/imdb_train_text.txtst" "./imdb/imdb_train_text.txtstp"
python3 process.py "./imdb/imdb_test_text.txtst" "./imdb/imdb_test_text.txtstp"  
python3 train.py "./imdb/imdb_train_text.txtstp" "./imdb/imdb_train_labels.txt" "learned_st_p.txt"
echo "stp done"

python3 process_e_1.py "./imdb/imdb_train_text.txtst" "./imdb/imdb_train_text.txtstp1"
python3 process_e_1.py "./imdb/imdb_test_text.txtst" "./imdb/imdb_test_text.txtstp1"  
python3 train.py "./imdb/imdb_train_text.txtstp1" "./imdb/imdb_train_labels.txt" "learned_st_p1.txt"
echo "stp1 done"

python3 process_e_2.py "./imdb/imdb_train_text.txtst" "./imdb/imdb_train_text.txtstp2"
python3 process_e_2.py "./imdb/imdb_test_text.txtst" "./imdb/imdb_test_text.txtstp2"  
python3 train.py "./imdb/imdb_train_text.txtstp2" "./imdb/imdb_train_labels.txt" "learned_st_p2.txt"
echo "stp2 done"

python3 process_e_3.py "./imdb/imdb_train_text.txtst" "./imdb/imdb_train_text.txtstp3"
python3 process_e_3.py "./imdb/imdb_test_text.txtst" "./imdb/imdb_test_text.txtstp3"  
python3 train.py "./imdb/imdb_train_text.txtstp3" "./imdb/imdb_train_labels.txt" "learned_st_p3.txt"
echo "stp3 done"

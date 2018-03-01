import csv
import math
from random import randint
import sys

# 0 for unstemmed, single word features
# 1 for stemmed, single word features
# 2 for unstemmed, single word features
# 3 for stemmed, single word features

learnedfile = ""
if(sys.argv[1] == '0'):
	learnedfile = "learned_p.txt"
elif(sys.argv[1] == '1'):
	learnedfile = "learned_st_p.txt"
elif(sys.argv[1] == '2'):
	learnedfile = "learned_p1.txt"
elif(sys.argv[1] == '3'):
	learnedfile = "learned_st_p1.txt"

csvfile = open(learnedfile, 'r')
data = list(csv.reader(csvfile, delimiter=' '))

classes=len(data[0])
lbl=[]
phi=[]
for j in range(classes):
	lbl.append(int(data[0][j]))
	phi.append(float(data[1][j]))

invert = [-1 for i in range(max(lbl)+2)]
for j in range(classes):
	invert[lbl[j]] = j

theta={}
for i in range(2,len(data)):
	word = data[i][0]
	theta[word]=[]
	for j in range(1,classes+1):
		theta[word].append(float(data[i][j]))

def print_conf(confusion):
	print(" ")
	s="  "
	for j in range(classes):
		s+=str(lbl[j])+" "
	print(s)

	for j in range(classes):
		s = str(lbl[j])+" "
		for i in range(classes):
			s+=str(confusion[j][i])+" "
		print(s)	 

def predict(textfile, labelfile):
	csvfile = open(textfile, 'r')
	data = list(csv.reader(csvfile, delimiter=' '))

	csvfile = open(labelfile, 'r')
	labels = list(csv.reader(csvfile))

	mtest = len(labels)
	print("{} instances".format(mtest))

	confusion=[[0 for j in range(classes)] for i in range(classes)]

	for i in range(mtest):
		labels[i] = int(labels[i][0])

	o = [0 for i in range(max(labels)+1)]
	countmo = 0
	for i in range(mtest):
		o[labels[i]] += 1
		if(o[labels[i]] > countmo):
			mo = labels[i]
			countmo = o[labels[i]]


	correct_nb = 0
	correct_mo = 0
	correct_ran = 0

	t = 0
	dtest = [{}, {}]
	for a in data:
		# print(a)
		if(len(a) == 1):

			bestj = -1
			mt = -10000000000000000
			for j in range(classes):
				temp = math.log(phi[j])

				for word in dtest[t]:
					try:
						temp += math.log(theta[word][j])*dtest[t][word]
					except KeyError:
						donothing = 0

				if(j == 0):
					bestj = 0
					mt = temp
				if(temp > mt):
					mt = temp
					bestj = j

# t is 0 based

			confusion[invert[labels[t]]][bestj] += 1
			if(lbl[bestj] == labels[t]):
				correct_nb += 1
			if(lbl[randint(0, classes-1)] == labels[t]):
				correct_ran += 1
			if(mo == labels[t]):
				correct_mo += 1

			dtest.append({})
			t += 1

		else:
			dtest[t][a[0]] = int(a[1])

	assert (t==mtest)		
	print("Using Naive Bayes        :\t{} correct  {}%".format(correct_nb, (correct_nb/mtest)*100))
	print("Using Random class       :\t{} correct  {}%".format(correct_ran, (correct_ran/mtest)*100))
	print("Using Most Occuring class:\t{} correct  {}%".format(correct_mo, (correct_mo/mtest)*100))

	print_conf(confusion)

if(sys.argv[1] == '0'):
	# testing on training set
	print("testing on training set")
	predict("./imdb/imdb_train_text_p.txt", "./imdb/imdb_train_labels.txt")
	print("")

	# testing on testing set
	print("testing on testing set")
	predict("./imdb/imdb_test_text_p.txt", "./imdb/imdb_test_labels.txt")
	print("")

elif(sys.argv[1]=='1'):

	# testing on testing set
	print("testing on stemmed testing set")
	predict("./imdb/imdb_test_text_st_p.txt", "./imdb/imdb_test_labels.txt")
	print("")

elif(sys.argv[1] == '2'):

	# testing on testing set
	print("testing on testing set")
	predict("./imdb/imdb_test_text_p1.txt", "./imdb/imdb_test_labels.txt")
	print("")

elif(sys.argv[1] == '3'):

	# testing on testing set
	print("testing on testing set")
	predict("./imdb/imdb_test_text_st_p1.txt", "./imdb/imdb_test_labels.txt")
	print("")

import csv
import math
from random import randint
import sys

# calculate accuracy, print confusion matrix, 

if(sys.argv[1] =='1'):
	print("Naive Bayes with no stemming")
elif(sys.argv[1] == '2'):
	print("Naive Bayes with stemming")
elif(sys.argv[1] == '3'):
	print("Naive Bayes with stemming and bi grams")
elif(sys.argv[1] == '4'):
	print("Naive Bayes with stemming and tri grams")
elif(sys.argv[1] == '5'):
	print("Naive Bayes with stemming and 4 gram")
# elif(sys.argv[1] == '6'):
# 	print("Random prediction")
# elif(sys.argv[1] == '7'):
# 	print("Most occuring in test data")


csvfile = open(sys.argv[2], 'r')
predictions = list(csv.reader(csvfile))

csvfile = open(sys.argv[3], 'r')
labels = list(csv.reader(csvfile))

assert len(predictions)==len(labels)

csvfile = open(sys.argv[4], 'r')
learnedfile = list(csv.reader(csvfile, delimiter=' '))

classes = len(learnedfile[0])
lbl = []
for j in range(classes):
	lbl.append(int(learnedfile[0][j]))

invert = [-1 for i in range(max(lbl)+2)]
for j in range(classes):
	invert[lbl[j]] = j


confusion = [[0 for j in range(classes)] for i in range(classes)]

m=len(labels)
correct = 0
for i in range(m):
	p=int(predictions[i][0])
	a=int(labels[i][0])
	
	if(p==a):
		correct+=1
	confusion[invert[a]][invert[p]]+=1


def print_conf(confusion):
	print(" ")
	s = "$,"
	for j in range(classes):
		s += str(lbl[j])+","
	print(s)

	for j in range(classes):
		s = str(lbl[j])+","
		for i in range(classes):
			s += str(confusion[j][i])+","
		print(s)

print("accuracy={}%".format((correct/m)*100))
print_conf(confusion)

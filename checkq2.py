import csv
import math
from random import randint, shuffle
import sys
import numpy as np


if(sys.argv[1] == '1'):
	print("Pegasos")
elif(sys.argv[1] == '2'):
	print("multi class linear SVM")
elif(sys.argv[1] == '3'):
	print("Gaussian Cross validation with best C")


csvfile = open(sys.argv[2], 'r')
predictions = list(csv.reader(csvfile))

csvfile = open(sys.argv[3], 'r')
labels = list(csv.reader(csvfile))

assert len(predictions) == len(labels)

m = len(labels)
correct = 0
for i in range(m):
	p = int(predictions[i][0])
	a = int(labels[i][0])

	if(p == a):
		correct += 1

print("Accuracy={}%".format((correct/m)*100))


def confusion(predicted, actual):
	classes = 10

	c = [[0 for i in range(classes)] for j in range(classes)]
	t = 0
	for i in range(m):
		a = int(actual[i][0])
		p = int(predicted[i][0])
		c[a][p] += 1
		if(t < 5 and a != p):
			t += 1
			print("Miss prediction {} actual={} predicted={}".format(i+1,a,p))
	s = "$,"
	for j in range(classes):
		s += str(j)+","
	print(s)
	for i in range(classes):
		s = str(i)+","
		for j in range(classes):
			s += str(c[i][j])+","
		print(s)


if(sys.argv[1] == '3'):
	confusion(predictions,labels)
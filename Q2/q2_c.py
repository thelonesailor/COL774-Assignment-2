import csv
import sys
import numpy as np
from random import shuffle


inputfile = "train.csv"
csvfile = open(inputfile, 'r')
data = list(csv.reader(csvfile))
shuffle(data)

m = len(data)
n = len(data[0])-1
xtrain=[]
ytrain=[]
for i in range(m):
	for j in range(n+1):
		data[i][j] = int(data[i][j])
	
	mi = 3000
	ma = -1
	for j in range(n):
		p = data[i][j]
		if(p < mi):
			mi = p
		if(p > ma):
			ma = p

	for j in range(n):
		data[i][j] = float(data[i][j]-mi)/(ma-mi)

	image = data[i]
	ytrain.append(image[n])
	xtrain.append(image[:n])


inputfile = "test.csv"
csvfile = open(inputfile, 'r')
data = list(csv.reader(csvfile))
shuffle(data)

m = len(data)
n = len(data[0])-1
ytest = []
xtest = []
for i in range(m):
	for j in range(n+1):
		data[i][j] = int(data[i][j])
	
	mi=3000
	ma=-1
	for j in range(n):
		p=data[i][j]
		if(p<mi):mi=p
		if(p>ma):ma=p	

	for j in range(n):
		data[i][j] = float(data[i][j]-mi)/(ma-mi)
	
	image = data[i]
	ytest.append(image[n])
	xtest.append(image[:n])



from svmutil import svm_train,svm_predict

print("Linear")
mlinear = svm_train(ytrain, xtrain, '-s 0 -t 0 -c 1 -q')
p_label, p_acc, p_val = svm_predict(ytest, xtest, mlinear)
# a,b,c=p_acc
# print(p_acc)
print("\nGaussian")
mgaussian = svm_train(ytrain, xtrain, '-s 0 -t 2 -c 1 -g 0.05 -q')
p_label, p_acc, p_val = svm_predict(ytest, xtest, mgaussian)

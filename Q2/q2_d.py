import csv
import sys
import numpy as np
from random import shuffle

inputfile = "train.csv"
csvfile = open(inputfile, 'r')
data = list(csv.reader(csvfile))
shuffle(data)

md = len(data)
n = len(data[0])-1
xtrain=[]
ytrain=[]
for i in range(md):
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
# don't shuffle test data

mtest = len(data)
n = len(data[0])-1
ytest = []
xtest = []
for i in range(mtest):
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

def confusion(predicted,actual):
	classes=10
	
	c=[[0 for i in range(classes)] for j in range(classes)]
	t=0
	for i in range(mtest):
		a = actual[i]
		p = int(predicted[i])
		c[a][p] += 1
		if(t<5 and a!=p):
			t+=1
			print("Miss prediction {}".format(i))
	s="$,"
	for j in range(classes):
		s+=str(j)+","
	print(s)
	for i in range(classes):
		s=str(i)+","
		for j in range(classes):
			s += str(c[i][j])+","
		print(s)	



for c in [0.00001, 0.001, 1, 5, 10]:
	print("\nGaussian C={}".format(c))
	sys.stdout.flush()
	
	mgaussian = svm_train(ytrain, xtrain,
	                      '-s 0 -t 2 -c {} -g 0.05 -v 10 -q'.format(c))

	mgaussian = svm_train(ytrain, xtrain,
	                      '-s 0 -t 2 -c {} -g 0.05 -q'.format(c))
	p_label, p_acc, p_val = svm_predict(ytest, xtest, mgaussian)
	confusion(p_label,ytest)

	f=open("predictionsQ2d_{}.txt".format(c),'w')
	for i in range(mtest):
		print(int(p_label[i]),file=f)
	f.close()	
	
	sys.stdout.flush()

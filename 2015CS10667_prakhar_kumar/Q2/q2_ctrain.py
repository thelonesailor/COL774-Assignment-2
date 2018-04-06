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

f=open("scalingq2_c.txt",'w')
for j in range(n):	
	mi = 3000
	ma = -1
	for i in range(m):
		p = data[i][j]
		if(p < mi):
			mi = p
		if(p > ma):
			ma = p

	for i in range(m):
		if(ma-mi>0):
			data[i][j] = float(data[i][j]-mi)/(ma-mi)
	
	print(str(mi)+" "+str(ma),file=f)	
f.close()

for i in range(m):
	image = data[i]
	ytrain.append(image[n])
	xtrain.append(image[:n])



from svmutil import svm_train, svm_predict, svm_save_model

print("Linear")
mlinear = svm_train(ytrain, xtrain, '-s 0 -t 0 -c 1 -q')
svm_save_model('q2_c_linear.model', mlinear)

# p_label, p_acc, p_val = svm_predict(ytrain, xtrain, mlinear)

print("\nGaussian")
mgaussian = svm_train(ytrain, xtrain, '-s 0 -t 2 -c 1 -g 0.05 -q')
svm_save_model('q2_c_gaussian.model', mgaussian)

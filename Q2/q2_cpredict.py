import csv
import sys
import numpy as np
from random import shuffle


inputfile = sys.argv[1]
csvfile = open(inputfile, 'r')
data = list(csv.reader(csvfile))

m = len(data)
n = len(data[0])
print(m)
ytest = []
xtest = []
for i in range(m):
	for j in range(n):
		data[i][j] = int(data[i][j])

csvfile = open("./Q2/scalingq2_c.txt", 'r')
scale = list(csv.reader(csvfile,delimiter=' '))
for j in range(n):
	mi=int(scale[j][0])
	ma=int(scale[j][1])
	
	for i in range(m):
		if(ma-mi > 0):
			data[i][j] = float(data[i][j]-mi)/(ma-mi)


for i in range(m):
	image = data[i]
	ytest.append(-1)
	xtest.append(image)


from svmutil import svm_train, svm_predict, svm_load_model 

# model = svm_load_model('./Q2/q2_c_gaussian.model')
model = svm_load_model('./Q2/q2_c_linear.model')
p_label, p_acc, p_val = svm_predict(ytest, xtest, model)

assert len(p_label)==m

f=open(sys.argv[2],'w')
for i in range(len(p_label)):
	print(int(p_label[i]),file=f)

f.close()

import csv
import sys
import numpy as np
from random import shuffle


inputfile = sys.argv[1]
csvfile = open(inputfile, 'r')
data = list(csv.reader(csvfile))
# don't shuffle test data

mtest = len(data)
n = len(data[0])
ytest = []
xtest = []
for i in range(mtest):
	for j in range(n):
		data[i][j] = int(data[i][j])


csvfile = open("./Q2/scalingq2_d.txt", 'r')
scale = list(csv.reader(csvfile, delimiter=' '))
for j in range(n):
	mi = int(scale[j][0])
	ma = int(scale[j][1])

	for i in range(mtest):
		if(ma-mi > 0):
			data[i][j] = float(data[i][j]-mi)/(ma-mi)


for i in range(mtest):
	image = data[i]
	ytest.append(-1)
	xtest.append(image[:n])



from svmutil import svm_train, svm_predict, svm_load_model

c=5
print(c)
model = svm_load_model('./Q2/q2_d_gauss{}.model'.format(c))
p_label, p_acc, p_val = svm_predict(ytest, xtest, model)

f = open(sys.argv[2], 'w')
for i in range(len(p_label)):
	print(int(p_label[i]), file=f)

f.close()

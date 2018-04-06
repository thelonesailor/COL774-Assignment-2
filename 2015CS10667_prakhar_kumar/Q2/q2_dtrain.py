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

f = open("scalingq2_d.txt", 'w')
for j in range(n):
	mi = 3000
	ma = -1
	for i in range(md):	
		p = data[i][j]
		if(p < mi):
			mi = p
		if(p > ma):
			ma = p

	for i in range(md):
		if(ma-mi>0):
			data[i][j] = float(data[i][j]-mi)/(ma-mi)

	print(str(mi)+" "+str(ma), file=f)
f.close()

for i in range(md):
	image = data[i]
	ytrain.append(image[n])
	xtrain.append(image[:n])



	
from svmutil import svm_train,svm_predict,svm_save_model



# for c in [0.00001, 0.001, 1, 5, 10]:
# 	print("\nGaussian C={}".format(c))
# 	sys.stdout.flush()
	
# 	mgaussian = svm_train(ytrain, xtrain,
# 	                      '-s 0 -t 2 -c {} -g 0.05 -v 10 -q'.format(c))

# 	mgaussian = svm_train(ytrain, xtrain,
# 	                      '-s 0 -t 2 -c {} -g 0.05 -q'.format(c))
# 	# p_label, p_acc, p_val = svm_predict(ytest, xtest, mgaussian)
# 	# confusion(p_label,ytest)

# 	f=open("predictionsQ2d_{}.txt".format(c),'w')
# 	for i in range(mtest):
# 		print(int(p_label[i]),file=f)
# 	f.close()	
	
# 	sys.stdout.flush()

c=5
print("\nGaussian C={}".format(c))
sys.stdout.flush()

# mgaussian = svm_train(ytrain, xtrain,
# 						'-s 0 -t 2 -c {} -g 0.05 -v 10 -q'.format(c))

mgaussian = svm_train(ytrain, xtrain,
						'-s 0 -t 2 -c {} -g 0.05 -q'.format(c))
svm_save_model('q2_d_gauss{}.model'.format(c), mgaussian)

sys.stdout.flush()

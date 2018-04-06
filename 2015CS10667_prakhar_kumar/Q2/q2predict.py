import csv
import math
from random import randint, shuffle
import sys
import numpy as np

classes=10
para = [[0 for i in range(classes)] for j in range(classes)]

learnedfile = sys.argv[1]
csvfile = open(learnedfile, 'r')
parameter = list(csv.reader(csvfile))

n = int(parameter[0][0])
u=1
# for u in range(1,len(parameter)):
while(u < len(parameter)):
	# print(u)
	i = int(parameter[u][0])
	j = int(parameter[u][1])
	b = float(parameter[u][2])
	
	w = []
	# float(parameter[u][2])
	for k in range(u+1,u+n+1):
		w.append(float(parameter[k][0]))
	u+=(n+1)

	para[i][j] = (w,b)

for i in range(classes):
	for j in range(i+1, classes):
		assert para[i][j]!=0

def svmpredict(testfile,outfile):

	out=open(outfile,'w')

	csvfile = open(testfile, 'r')
	data = list(csv.reader(csvfile))
	mtest = len(data)

	for i in range(mtest):
		# image = data[i]
		# assert n == (len(image)-1)
		for j in range(n):
			data[i][j] = int(data[i][j])

	correct = 0
	print("{} instances".format(mtest))
	for j in range(n):
		# image = data[u]
		# x = image[:n]

		mi = 3000
		ma = -1
		for u in range(mtest):
			p = data[u][j]
			if(p < mi):
				mi = p
			if(p > ma):
				ma = p

		for u in range(mtest):
			if(ma-mi>0):
				data[u][j] = (data[u][j]-mi)/(ma-mi)

	for u in range(mtest):
		# y = image[n]
		x = data[u][:n]
		bcl = [0 for i in range(classes)]
		for i in range(classes):
			for j in range(i+1, classes):
				(w, b) = para[i][j]
				temp = np.dot(w, x)+b
				if(temp > 0):
					bcl[i] += 1
				elif(temp <= 0):
					bcl[j] += 1

		maxi = -1
		maxb = -1
		for i in range(classes):
			if(bcl[i] >= maxb):
				maxb = bcl[i]
				maxi = i
		print(maxi,file=out)		
		# if(maxi == y):
		# 	correct += 1
	out.close()
	# print("{} correct\t{}%\n".format(correct, (correct/mtest)*100))

datafile=sys.argv[2]
outfile = sys.argv[3]

print("predictng values")
svmpredict(datafile,outfile)

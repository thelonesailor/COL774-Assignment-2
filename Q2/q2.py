import csv
import math
from random import randint,shuffle
import sys
import numpy as np


trainfile="train.csv"
csvfile = open(trainfile, 'r')
data = list(csv.reader(csvfile))

shuffle(data)

m=len(data)
n = len(data[0])-1
for i in range(m):
	image=data[i]
	assert n==(len(image)-1)
	for j in range(len(image)):
		data[i][j]=int(data[i][j])

	mi=3000
	ma=-1
	for j in range(len(image)-1):
		p = data[i][j]
		if(p < mi):
			mi = p
		if(p > ma):
			ma = p
	for j in range(len(image)-1):
		data[i][j] = (data[i][j]-mi)/(ma-mi)

Xo=[]
Yo=[]
for image in data:
	l=len(image)
	Xo.append(image[:l-1])
	Yo.append(image[l-1])

Xo=np.array(Xo)

def train(cx,cy):

	Y = []
	X = []
	for i in range(m):
		if(Yo[i] == cx):
			X.append(Xo[i])
			Y.append(1)
		elif(Yo[i] == cy):
			X.append(Xo[i])
			Y.append(-1)

	
	w=np.zeros(n)
	b=0

	T=2000 #number of iterations
	C=1
	k=100
	t=1
	while(t<T):
		A=np.random.choice(len(X), k, replace=False)
		
		At=[]
		for i in A:
			ti=1-Y[i]*(np.matmul(w.T,X[i])+b)
			if(ti>=0):
				At.append(i)


		etaw=1/t		
		grad=0
		for i in At:
			grad-=Y[i]*X[i]
		w = (1-etaw)*w - C*etaw*grad


		etab=1/t
		gradient = 0
		for i in At:
			gradient -= Y[i]
		b = b - etab*C*gradient

		t+=1

	return (w,b)


classes=10
para=[[0 for i in range(classes)] for j in range(classes)]
for i in range(classes):
	for j in range(i+1,classes):
		print((i,j))
		para[i][j]=train(i,j)


print("training done\n")

def svmpredict(testfile):

	csvfile = open(testfile, 'r')
	data = list(csv.reader(csvfile))
	mtest = len(data)

	for i in range(mtest):
		image = data[i]
		# assert n == (len(image)-1)
		for j in range(n+1):
			data[i][j] = int(data[i][j])


	correct=0
	print("{} instances".format(mtest))
	for u in range(mtest):
		image=data[u]
		x=image[:n]

		mi = 3000
		ma = -1
		for j in range(n):
			p = x[j]
			if(p < mi):
				mi = p
			if(p > ma):
				ma = p
		for j in range(n):
			x[j]=(x[j]-mi)/(ma-mi)

		y=image[n]
		bcl=[0 for i in range(classes)]
		for i in range(classes):
			for j in range(i+1, classes):
				(w,b)=para[i][j]
				temp=np.dot(w,x)+b
				if(temp>0):
					bcl[i]+=1
				elif(temp<=0):
					bcl[j]+=1

		maxi=-1
		maxb=-1
		for i in range(classes):
			if(bcl[i]>=maxb):
				maxb=bcl[i]
				maxi=i
		if(maxi==y):correct+=1

	print("{} correct\t{}%\n".format(correct,(correct/mtest)*100))		

print("testing on training data")
svmpredict("train.csv")

print("testing on testing data")
svmpredict("test.csv")

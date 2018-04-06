import csv
import math
from random import randint,shuffle
import sys
import numpy as np


trainfile=sys.argv[1]
csvfile = open(trainfile, 'r')
data = list(csv.reader(csvfile))

shuffle(data)

m=len(data)
n = len(data[0])-1
for i in range(m):
	image=data[i]
	assert n==(len(image)-1)
	for j in range(n+1):
		data[i][j]=int(data[i][j])


for j in range(n):
	mi=3000
	ma=-1
	for i in range(m):
		p = data[i][j]
		if(p < mi):
			mi = p
		if(p > ma):
			ma = p

	for i in range(m):
		if(ma-mi>0):
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
learnedfile = sys.argv[2]
out=open(learnedfile,'w')
print(n,file=out)
for i in range(classes):
	for j in range(i+1, classes):
		w,b=para[i][j]
		print("{},{},{}".format(i,j,b),file=out)
		for a in range(len(w)):
			print(w[a],file=out)


out.close()

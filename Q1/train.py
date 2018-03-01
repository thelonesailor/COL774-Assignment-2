import csv
import math
from random import randint 
import sys

# 1 for stemmed
# 0 for unstemmed
inputfile=""
if(sys.argv[1] == '1'):
	inputfile = "./imdb/imdb_train_text_st_p.txt"
else:
	inputfile = "./imdb/imdb_train_text_p.txt"


csvfile = open(inputfile, 'r')
data = list(csv.reader(csvfile,delimiter=' '))

d=[{},{}]
vocabulary={}
count=[0,0]
t=1
for a in data:
	# print(a)
	if(len(a)==1):
		t+=1
		d.append({})
		count.append(0)
	else:	
		d[t][a[0]] = int(a[1])
		vocabulary[a[0]]=1
		count[t]+=int(a[1])

m1=t-1

csvfile = open("./imdb/imdb_train_labels.txt", 'r')
labels = list(csv.reader(csvfile))
m2=len(labels)

assert m1==m2
m=m1

# 8 classes
lbl=[]

for i in range(m):
	labels[i] = int(labels[i][0])
	if(labels[i] not in lbl):
		lbl.append(labels[i])
# print(labels)
lbl=sorted(lbl)
print(lbl)
classes=len(lbl) 

invert = [-1 for i in range(max(lbl)+2)]
for j in range(classes):
	invert[lbl[j]] = j

# constant for laplace smoothing
c=1
V=len(vocabulary)
print("{} words in training data\n".format(V))

phi=[0 for i in range(classes)]
for i in range(m):
	for j in range(classes):
		if(labels[i]==lbl[j]):
			phi[j]+=1
			break
for j in range(classes):
	phi[j] /= m


ex=[[] for j in range(classes)]
for j in range(classes):
	for i in range(m):
		if(labels[i] == lbl[j]):
			ex[j].append(i)

t=1
theta={}
for word in vocabulary:
	theta[word]=[0 for j in range(classes)]
	num = [0 for j in range(classes)]
	denom = [0 for j in range(classes)]

	
	for j in range(classes):	
		# fill theta[word][j]
		num=c
		denom=V*c
		for i in ex[j]:
			try:
				num+=d[i][word]
			except KeyError:
				donothing = 0

			denom+=count[i]

		theta[word][j]=num/denom
	# break

	print(t)
	t+=1	

print("training done")
# training done

learnedfile=""
if(sys.argv[1]=='1'):
	learnedfile="learned_st1.txt"
else:
	learnedfile = "learned1.txt"

f=open(learnedfile,'w')

s=""
for j in range(classes):
	s+=str(lbl[j])
	if(j<classes-1):
		s+=" "
print(s,file=f)
s=""
for j in range(classes):
	s+=str(phi[j])
	if(j < classes-1):
		s += " "
print(s, file=f)

for word in vocabulary:
	s=word+" "
	for j in range(classes):
		s += str(theta[word][j])+" "
		
	print(s,file=f)
	# break	
f.close()




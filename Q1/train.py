import csv
import math
from random import randint 
import sys

# 0 for unstemmed
# 1 for stemmed
# 2 for unstemmed
# 3 for stemmed

inputfile=sys.argv[1]
# if(sys.argv[1] == '0'):
# 	inputfile = "./imdb/imdb_train_text_p.txt"
# elif(sys.argv[1] == '1'):
# 	inputfile = "./imdb/imdb_train_text_st_p.txt"
# elif(sys.argv[1] == '2'):
# 	inputfile = "./imdb/imdb_train_text_st_p1.txt"
# elif(sys.argv[1] == '3'):
# 	inputfile = "./imdb/imdb_train_text_st_p2.txt"
# elif(sys.argv[1] == '4'):
# 	inputfile = "./imdb/imdb_train_text_st_p3.txt"
# elif(sys.argv[1] == '5'):
# 	inputfile = "./imdb/imdb_train_text_st_p4.txt"



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

csvfile = open(sys.argv[2], 'r')
labels = list(csv.reader(csvfile))
m2 = len(labels)

assert m1==m2
m=m1


# 8 classes
lbl = []

for i in range(m):
	labels[i] = int(labels[i][0])
	if(labels[i] not in lbl):
		lbl.append(labels[i])
# print(labels)
lbl = sorted(lbl)
print(lbl)
classes = len(lbl)

invert = [-1 for i in range(max(lbl)+2)]
for j in range(classes):
	invert[lbl[j]] = j

# constant for laplace smoothing
c=1
num = {}
for word in vocabulary:
	num[word] = [c for j in range(classes)]

for i in range(1,m+1):
	for word in d[i]:
		num[word][invert[labels[i-1]]]+=d[i][word]

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

denom = [V*c for j in range(classes)]
for i in range(1,m+1):
	clas = invert[labels[i-1]]
	denom[clas] += count[i]



t=1
theta={}
for word in vocabulary:
	theta[word]=[0 for j in range(classes)]
	for j in range(classes):
		theta[word][j]=num[word][j]/denom[j]
	# print(t)
	t+=1


print("training done")
# training done

learnedfile=sys.argv[3]
# if(sys.argv[1] == '0'):
# 	learnedfile = "learned_p.txt"
# elif(sys.argv[1] == '1'):
# 	learnedfile="learned_st_p.txt"
# elif(sys.argv[1] == '2'):
# 	learnedfile = "learned_st_p1.txt"
# elif(sys.argv[1] == '3'):
# 	learnedfile = "learned_st_p2.txt"
# elif(sys.argv[1] == '4'):
# 	learnedfile = "learned_st_p3.txt"
# elif(sys.argv[1] == '5'):
# 	learnedfile = "learned_st_p4.txt"

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




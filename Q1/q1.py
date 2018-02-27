import csv

csvfile = open("./imdb/imdb_train_text_p.txt", 'r')
data = list(csv.reader(csvfile,delimiter=' '))

d=[{},{}]

t=1
for a in data:
	# print(a)
	if(len(a)==1):
		t+=1
		d.append({})
	else:	
		d[t][a[0]] = int(a[1])
m1=t-1

csvfile = open("./imdb/imdb_train_labels.txt", 'r')
labels = list(csv.reader(csvfile))
m2=len(labels)

assert m1==m2
m=m1

for i in range(m):
	labels[i] = int(labels[i][0])
# print(labels)


# 8 classes
c=8 

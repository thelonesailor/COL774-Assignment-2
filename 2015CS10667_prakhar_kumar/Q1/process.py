from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

tokenizer = RegexpTokenizer(r'\w+')

def clean(inputfile, outputfile):
	docs=[]
	with open(inputfile) as f:
		docs = f.readlines()

	sys.stdout = open(outputfile, 'w')
	
	t=1
	for line in docs:
		raw=line
		raw = line.lower()
		raw = raw.replace(",", " ")
		raw = raw.replace(".", " ")
		raw = raw.replace("!", " ")
		raw = raw.replace("(", " ")
		raw = raw.replace(")", " ")
		raw = raw.replace("'", " ")
		raw = raw.replace("\"", " ")
		raw = raw.replace("-", " ")
		raw = raw.replace("/", " ")
		raw = raw.replace("<", " ")
		raw = raw.replace(">", " ")

		tokens = tokenizer.tokenize(raw)
		d={}
		for token in tokens:
			if(token in d):
				d[token]+=1
			else:
				d[token]=1

		for token in d:
			sys.stdout.write(token+" "+str(d[token])+"\n")

		t+=1
		sys.stdout.write("-1\n")

	sys.stdout.close()	


inputfile = sys.argv[1]
outputfile = sys.argv[2]
clean(inputfile,outputfile)
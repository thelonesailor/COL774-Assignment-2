from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

tokenizer = RegexpTokenizer(r'\w+')


def clean(inputfile, outputfile):
	docs = []
	with open(inputfile) as f:
		docs = f.readlines()

	sys.stdout = open(outputfile, 'w')

	t = 1
	for line in docs:
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
		d = {}
		l = len(tokens)
		for i in range(0,l,1):
			# print(i)
			if(i<l-1):
				token=tokens[i]+tokens[i+1]
			else:
				break
				token = tokens[i]

			# print(token)
			if(token in d):
				d[token] += 1
			else:
				d[token] = 1

		for token in d:
			if(d[token] > 1):
				sys.stdout.write(token+" "+str(d[token])+"\n")

		t += 1
		sys.stdout.write("-1\n")

	sys.stdout.close()


# inputfile = "./imdb/imdb_train_text.txt"
# outputfile = "./imdb/imdb_train_text_p2.txt"
# clean(inputfile, outputfile)

# inputfile = "./imdb/imdb_test_text.txt"
# outputfile = "./imdb/imdb_test_text_p2.txt"
# clean(inputfile, outputfile)

inputfile = "./imdb/imdb_train_text_st.txt"
outputfile = "./imdb/imdb_train_text_st_p2.txt"
clean(inputfile, outputfile)

inputfile = "./imdb/imdb_test_text_st.txt"
outputfile = "./imdb/imdb_test_text_st_p2.txt"
clean(inputfile, outputfile)

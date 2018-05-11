import csv
import math
from random import randint, shuffle
import sys
import numpy as np


def split(filegiven,fileimage,filelabels): 
	csvfile = open(filegiven, 'r')
	data = list(csv.reader(csvfile))
	n=len(data[0])-1

	fi=open(fileimage,'w')
	fl=open(filelabels,'w')

	for i in range(len(data)):
		s=""
		for j in range(n):
			s+=data[i][j]
			if(j<n-1):
				s+=","

		print(s,file=fi)
		print(data[i][n],file=fl)

	fl.close()
	fi.close()

split("train.csv","train_image.csv","train_label.csv")
split("test.csv", "test_image.csv", "test_label.csv")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # chart library
import math

def readData():
	dataSet = pd.read_csv("dataset.csv",delimiter =',')
	return dataSet

def entropy(class_sample):
	tmp = []
	for i in range(len(class_sample)):
		if tmp == []:
			tmp.append(class_sample[i])
		else:
			count = 0
			for j in range(len(tmp)):
				if tmp[j] == class_sample[i]:
					count += 1
			if count < 1:
				tmp.append(class_sample[i])
				
	# for i in range(1,class_sample+1):
		
		# tmp += (-class_sample[i]*(math.log(class_sample[i],2)))
	return tmp  

def information_gain(S, A):
	for i in range(len(A)):
		pass

if __name__ == '__main__':
	data = readData()
	print(entropy(data['kelayakan']))

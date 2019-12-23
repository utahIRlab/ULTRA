import os,sys
import json

DATA_PATH = sys.argv[1]
FILE_NAMES = ['train.txt', 'test.txt', 'valid.txt']

feature_scale = []

for f in FILE_NAMES:
	with open(DATA_PATH + f) as fin:
		for line in fin:
			arr = line.strip().split(' ')
			for i in range(len(arr)-2):
				arr2 = arr[i+2].split(':')
				idx = int(arr2[0])-1
				value = float(arr2[1])
				feature_scale += [None for k in range(idx - len(feature_scale) + 1)]
				if feature_scale[idx] == None:
					feature_scale[idx] = [value, value] #(min, max)
				else:
					if value > feature_scale[idx][1]:
						feature_scale[idx][1] = value
					if value < feature_scale[idx][0]:
						feature_scale[idx][0] = value

#output results
with open(DATA_PATH + 'feature_scale.json', 'w') as fout:
	json.dump(feature_scale, fout)
#print(feature_scale)

#195 VALUES 
#17 ROWS
#979 MAX
#7 MIN

import time
import sys
import numpy as np

#create hashtable of size 'size'
def createHashTable(size):
	hashTable = {}
	for i in range(size):
		hashTable[i] = 0
	return hashTable

#return hash address for itemSet
def hashItemSets(x, y):
	return(((x * 10) + y) % 7)

#create hash table 'L'
def createL(line):
	array = line.split(" ")
	for i in range (len(array) - 1):
		L[int(array[i])] += 1
		for j in range (i + 1, len(array) - 1):
			address = hashItemSets(int(array[i]), int(array[j]))
			itemSetHash[address] += 1

#write candidate
def createCandidate(line, minSupp, candidate):
	array = line.split(" ")
	for i in range (len(array) - 1):
		if (L[int(array[i])] < minSupp):
			continue
		else:
			for j in range (i + 1, len(array) - 1):
				if (L[int(array[j])] >= minSupp):
					address = hashItemSets(int(array[i]), int(array[j]))
					if (itemSetHash[address] >= minSupp):
						print(i, j)


def apriori(inp, out, minSupp,):
	global itemSetHash, L
	itemSetHash = createHashTable(10000)	#This should be set to the estimated highest value of your hash table
	L = createHashTable(2000)	#This should be set to the highest value in the file
	with open(inp) as data:
		for line in data:
			createL(line)

	with open(inp) as data:
		candidate = open(out, 'w')
		for line in data:
			print(line)
			createCandidate(line, minSupp, candidate)

def main():
	inp = str(sys.argv[1])
	out = str(sys.argv[2])
	minSupp = int(sys.argv[3])
	apriori(inp, out, minSupp)

start_time = time.time()
main()
print(time.time() - start_time)




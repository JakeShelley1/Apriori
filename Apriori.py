#195 VALUES 
#17 ROWS
#979 MAX
#7 MIN

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


def apriori(inp, minSupp, out):
	global itemSetHash, L
	itemSetHash = createHashTable(2000)
	L = createHashTable(980)
	with open(inp) as data:
		for line in data:
			createL(line)

	with open(inp) as data:
		candidate = open(out, 'w')
		for line in data:
			print(line)
			createCandidate(line, minSupp, candidate)


apriori('T10I4D100KTest.dat', 2, 'candidate.dat')




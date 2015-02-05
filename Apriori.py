#195 VALUES 
#17 ROWS
#979 MAX
#7 MIN

import numpy as np

def createHashTable(size):
	hashTable = {}
	for i in range(size):
		hashTable[i] = 0
	return hashTable

def findItemSets()
	

def parseLine(line):
	array = line.split(" ")
	for i in range (len(array) - 1):
		L[int(array[i])] += 1
		for j in range (i + 1, len(array) - 1) 

with open('T10I4D100KTest.dat') as data:
	#Create hashes of estimated size
	itemSetHash = createHashTable(2000)
	L = createHashTable(980)
	for line in data:
		n = parseLine(line)
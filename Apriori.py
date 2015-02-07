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

#hash function for 'itemSetHash'
def getHashAddress(array):
	k = int(array[0])*10
	for i in array:
		k = k + int(i)
	k = k % 37173
	return k
		 
#fill hashtables		 
def createLAnditemSetHash(line):
	array = line.split(" ")
	for i in range (len(array) - 1):
		L[int(array[i])] += 1
		for j in range (i + 1, len(array) - 1):
			sliceArray = array[i:j+1]
			address = getHashAddress(sliceArray)
			itemSetHash[address] += 1

#write candidate
def createCandidate(line, minSupp, candidate):
	array = line.split(" ")
	for i in range (len(array) - 1):
		badValue = False
		if (L[int(array[i])] < minSupp):
			continue
		else:
			for j in range (i + 1, len(array) - 1):
				if (badValue):	#break if a value between i and j is not within minSupp
					break
				else:
					if (L[int(array[j])] < minSupp):
						badValue = True
					else:
						sliceArray = array[i:j+1]					
						address = getHashAddress(sliceArray)
						if (itemSetHash[address] >= minSupp):
							for n in range(len(sliceArray)):
								if (n == len(sliceArray) - 1):
									candidate.write(str(sliceArray[n]))
								else:
									candidate.write(str(sliceArray[n]) + ", ")
							candidate.write(" (" + str(itemSetHash[int(address)]) + ")\n" )


def apriori(inp, out, minSupp,):
	global itemSetHash, L
	itemSetHash = createHashTable(40000)	#This should be set to the estimated highest value of your hash table
	L = createHashTable(1000)	#This should be set to the highest value in the file
	with open(inp) as data:
		for line in data:
			createLAnditemSetHash(line)

	candidate = open(out, 'w')
	candidate.write("Unique numbers:\n\n")
	for key in L:
		if (L[key] > minSupp):
			candidate.write(str(key) + " (" + str(L[key]) + ")\n" )

	candidate.write("\n\nItem Sets:\n\n")
	with open(inp) as data:
		for line in data:
			createCandidate(line, minSupp, candidate)
	candidate.close()

def main():
	inp = str(sys.argv[1])
	out = str(sys.argv[2])
	minSupp = int(sys.argv[3])
	apriori(inp, out, minSupp)

start_time = time.time()
main()
print(time.time() - start_time)
import time
import sys
from collections import Counter
from itertools import combinations

#Counts all sets greather than 2 using combinations
def countAllSets(array):
	for i in range(3, 6):	#Set the second parameter to the max size of itemsets you want to test
		for j in combinations(array, i):
			y = list(j)
			temp = " ".join(y)
			count[temp] +=1

#Count item sets with a size of 2
def countPairs(i, array):
	sliceArray = []
	sliceArray.append(array[i])
	for j in range(i+1, len(array)):
		sliceArray.append(array[j])
		temp = " ".join(sliceArray)
		count[temp] += 1
		sliceArray.remove(array[j])

#Iterate throguh the line
def countItemsAndPairs(array):
	for i in range (len(array)):
		count[array[i]] += 1
		countPairs(i, array)	

#Write the final candidate
def writeCandidate(minSupp, candidate):
	for i in count:
		if count[i] >= minSupp:
			candidate.write(i + " (" + str(count[i]) + ")\n")	

def apriori(inp, out, minSupp,):
	global count
	count = Counter()
	lineCount = 0
	with open(inp) as data:
		for line in data:
			array = line.split(" ")
			tempInt = len(array) - 1
			if (array[tempInt] == '\n' or array[tempInt] == ''):
				del array[tempInt]
			array.sort()
			countItemsAndPairs(array)
			countAllSets(array)
	candidate = open(out, 'w')
	writeCandidate(minSupp, candidate)
	candidate.close()
	
def main():
	inp = str(sys.argv[1])
	out = str(sys.argv[2])
	minSupp = int(sys.argv[3])
	apriori(inp, out, minSupp)

start_time = time.time()
main()
print(time.time() - start_time)
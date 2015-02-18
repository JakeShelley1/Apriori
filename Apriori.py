import time
import sys
from collections import Counter


def countSets(i, array):
	for j in range (i + 2, len(array)):
		sliceArray = array[i:j+1]
		sliceArray.sort()
		temp = " ".join(sliceArray)
		count[temp] += 1

def countPairs(i, array):
	sliceArray = []
	sliceArray.append(array[i])
	for j in range(i+1, len(array)):
		sliceArray.append(array[j])
		sliceArray.sort()
		temp = " ".join(sliceArray)
		count[temp] += 1
		sliceArray.remove(array[j])

def countItemsAndPairs(line):
	array = line.split(" ")
	tempInt = len(array) - 1
	if (array[tempInt] == '\n' or array[tempInt] == ''):
		del array[tempInt]
	for i in range (len(array)):
		count[array[i]] += 1
		countPairs(i, array)
		countSets(i, array)	

def writeCandidate(minSupp, candidate):
	for i in count:
		if count[i] >= minSupp:
			candidate.write(i + " (" + str(count[i]) + ")\n")	

def apriori(inp, out, minSupp,):
	global count
	count = Counter()
	with open(inp) as data:
		for line in data:
			countItemsAndPairs(line)
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
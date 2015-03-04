import time
import sys
from collections import Counter
from itertools import combinations


# def countItemsAndPairs(line):
# 	array = line.split(" ")
# 	tempInt = len(array) - 1
# 	if (array[tempInt] == '\n' or array[tempInt] == ''):
# 		del array[tempInt]
# 	for i in range (len(array)):
# 		count[array[i]] += 1
# 		countPairs(i, array)
# 		# countSets(i, array)	

# def countSets(i, array):
# 	for j in range (i + 2, len(array)):
# 		sliceArray = array[i:j+1]
# 		sliceArray.sort()
# 		temp = " ".join(sliceArray)
# 		count[temp] += 1

#count every combination of sets of 4

def doCombinations(array, multiplier):
	for j in combinations(array, len(array)-1):
		y = list(j)
		temp = " ".join(y)
		itemSetCount[temp] += (1 * multiplier)

def count4Set(array, multiplier):
	midArray = array[1:len(array)-1]
	del array[1:len(array)-1]
	for z in range(len(midArray)):
		tempArray = list(array)
		tempArray.insert(1, midArray[z])
		temp = " ".join(tempArray)
		itemSetCount[temp] += (1 * multiplier)

#count every combination of pairs + unique numbers
def countPairs(multiplier, array):
	for i in range(len(array)):
		itemSetCount[array[i]] += (1 * multiplier)
		for j in range(i+1, len(array)):
			sliceArray = [array[i]]
			sliceArray.append(array[j])
			sliceArray.sort()
			temp = " ".join(sliceArray)
			itemSetCount[temp] += (1 * multiplier)
			sliceArray = array[i:j+1]
			if len(sliceArray) == 3:
				temp = " ".join(sliceArray)
				itemSetCount[temp] += (1*multiplier)
			elif len(sliceArray) == 4:
				count4Set(sliceArray, multiplier)
			elif len(sliceArray) == 6:
				doCombinations(sliceArray, multiplier)
			else:
				break

#Count unique numbers for the candidate
def countUniqueNumbers(line):
	array = line.split(" ")
	tempInt = len(array) - 1
	if (array[tempInt] == '\n' or array[tempInt] == ''):
		del array[tempInt]
	for i in range (len(array)):
		uniqueCount[array[i]] += 1

#prune original table to create candidate
def createCandidateHash(line, minSupp):
	array = line.split(" ")	
	tempInt = len(array) - 1
	if (array[tempInt] == '\n' or array[tempInt] == ''):
		del array[tempInt]
	goodArray = []
	for i in array:
		if uniqueCount[i] >= minSupp:
			goodArray.append(i)
	goodArray.sort()
	temp = " ".join(goodArray)
	candidateCount[temp] += 1

#write the temporary candidate
def writeCandidate(candidate):
	for i in candidateCount:
		candidate.write(i + " " + str(candidateCount[i]) + " \n")

#write the final output
def writeOutput(candidate, minSupp):
	for i in itemSetCount:
		if itemSetCount[i] >= minSupp:
			candidate.write(i + " (" + str(itemSetCount[i]) + ")\n")

#
def createOutput(line, candidate, minSupp):
	array = line.split(" ")
	multiplier = int(array[len(array)-2])
	del array[len(array)-2: len(array)]
	countPairs(multiplier, array)
	writeOutput(candidate, minSupp)

def apriori(inp, out, minSupp):
	global uniqueCount, candidateCount, itemSetCount
	uniqueCount = Counter()
	candidateCount = Counter()
	itemSetCount = Counter()
	with open(inp) as data:
		for line in data:
			countUniqueNumbers(line)

	with open(inp) as data:
		for line in data:
			createCandidateHash(line, minSupp)
		candidate = open("temp.dat", 'w')
		writeCandidate(candidate)
		candidate.close()

	lineCount = 0
	with open("temp.dat") as data:
		candidate = open(out, 'w')
		for line in data:
			lineCount += 1
			if lineCount % 1000 == 0:
				print lineCount
			createOutput(line, candidate, minSupp)
		candidate.close()

	# candidate = open(out, 'w')
	# writeCandidate(minSupp, candidate)
	# candidate.close()

def main():
	inp = str(sys.argv[1])
	out = str(sys.argv[2])
	minSupp = int(sys.argv[3])
	apriori(inp, out, minSupp)

start_time = time.time()
main()
print(time.time() - start_time)
import time
import sys
from collections import Counter
from itertools import combinations

#Write the final candidate
def writeCandidate(out, minSupp):
	for i in count:
		if count[i] >= minSupp:
			out.write(i + " (" + str(count[i]) + ")\n")

#Counts all sets greather than 2 using combinations
def countAllSets(array, start):
	for j in combinations(array, start):
		y = list(j)
		temp = " ".join(y)
		count[temp] +=1			

#Prune table for values and sets that no longer fit minimum support
def pruneTable(table, start, minSupp):
	for z in range((len(table))):
		array = table[z]
		deleteArray = []
		for i in range(len(array)):
			deleteArray.append(True)
		for j in combinations(array, start):
			y = list(j)
			tempArray = " ".join(y)
			if (count[tempArray] >= minSupp):
				tempArray = tempArray.split(" ")
				for item in tempArray:
					deleteArray[array.index(item)] = False
		deletion = []
		for x in range(len(deleteArray)):
			if (deleteArray[x]):
				deletion.append(array[x])
		for item in deletion:
			array.remove(item)
		table[z] = array	
	return table

#Create initial table
def createDataTable(inp):
	table = []
	with open(inp) as data:
		for line in data:
			array = line.split(" ")
			tempInt = len(array) - 1
			if (array[tempInt] == '\n' or array[tempInt] == ''):
				del array[tempInt]
			array = map(int, array)
			array.sort()
			array = map(str, array)
			table.append(array)
	return table

def apriori(inp, out, minSupp):
	global count, singleCount, flag
	count = Counter()
	flag = True
	start = 1
	table = createDataTable(inp)
	while (flag):
		flag = False
		for array in table:
			countAllSets(array, start)
		table = pruneTable(table, start, minSupp)
		start += 1
		for check in table:
			if len(check) != 0:
				flag = True

	out = open(out, 'w')
	writeCandidate(out, minSupp)
	out.close()

def main():
	inp = str(sys.argv[1])
	out = str(sys.argv[2])
	minSupp = int(sys.argv[3])
	apriori(inp, out, minSupp)

start_time = time.time()
main()
print(time.time() - start_time)
import time
import sys
from linkedList import *

#hash function for 'itemSetHash'
def getHashAddress(array):
	k = int(array[0])*10
	for i in array:
		if i == '\n' or i == '':
			break
		k = k + int(i)
	k = k % 37173
	return k

def hashPairs(array):
	address = getHashAddress(array)
	temp = Node(array)
	if itemSetHash[address].head == None:
		itemSetHash[address].insert(temp)
	flag = itemSetHash[address].search(temp)
	if flag == -1:
		itemSetHash[address].insert(temp)

		 
#fill hashtables		 
def createLAnditemSetHash(line):
	array = line.split(" ")
	for i in range (len(array)):
		if array[i] == '\n' or array[i] == '':
			break
		L[int(array[i])] += 1
		for j in range (i + 1, len(array)):
			if array[i] == '\n' or array[i] == '':
				break
			sliceArray = array[i:j+1]
			hashPairs(sliceArray)

def iterateList(head, minSupp, candidate):
	while(head != None):
		if (head.count >= minSupp):
			for n in head.data:
				candidate.write(n + ", ")
			candidate.write("(" + str(head.count) + ")\n")
		if (head.next == None):
			break
		else:
			head = head.next



def createCandidate2(minSupp, candidate):
	for i in itemSetHash:
		if itemSetHash[i].head == None:
			continue
		else:
			iterateList(itemSetHash[i].head, minSupp, candidate)


#write candidate
def createCandidate(line, minSupp, candidate):
	array = line.split(" ")
	for i in range (len(array) - 1):
		if (L[int(array[i])] < minSupp):
			continue
		else:
			for j in range (i + 1, len(array) - 1):
				if (L[int(array[j])] < minSupp):
					i = j + 1
					break
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
	itemSetHash = {}
	for i in range(37174):
		itemSetHash[i] = linkedList()
	L = {}
	for i in range(1000):	#Set to the max value found in the dataset
		L[i] = 0

	with open(inp) as data:
		for line in data:
			createLAnditemSetHash(line)

	candidate = open(out, 'w')
	candidate.write("Unique numbers:\n\n")
	for key in L:
		if (L[key] >= minSupp):
			candidate.write(str(key) + " (" + str(L[key]) + ")\n" )

	candidate.write("\n\nItem Sets:\n\n")
	with open(inp) as data:
		createCandidate2(minSupp, candidate)
		#for line in data:
		 #	createCandidate(line, minSupp, candidate)
	candidate.close()

def main():
	inp = str(sys.argv[1])
	out = str(sys.argv[2])
	minSupp = int(sys.argv[3])
	apriori(inp, out, minSupp)

start_time = time.time()
main()
print(time.time() - start_time)
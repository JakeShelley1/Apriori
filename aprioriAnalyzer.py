import sys

def apriori(inp):
	set3Count = 0
	pairCount = 0
	set2Count = 0
	lineCount = 0
	unique = 0
	with open(inp) as data:
		for line in data:
			temp = line.split(" ")
			if len(temp) - 1 == 3:
				set3Count += 1
			elif len(temp) - 1 == 2:
				set2Count += 1
			elif len(temp) - 1 == 1:
				unique += 1
			lineCount += 1
	print unique
	print set2Count
	print set3Count
	print lineCount
	
def main():
	inp = str(sys.argv[1])
	apriori(inp)

main()
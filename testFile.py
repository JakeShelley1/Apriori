import numpy as np

# def write(line, f):
# 	for i in line:
# 		f.write(str(i) + " ")
# 	f.write("\n")


# output = 'candidate.dat'
# thelist = np.random.randint(10, size=10)
# thelist2 = np.random.randint(10, size=10)
# f = open(output, 'w')
# write(thelist, f)
# write(thelist2, f)
# f.close()

# with open(output) as data:
# 	for line in data:
# 		print(line.split(" "))
# 	#this works^
dict1 = {10}
for i in dict1:
	i = 0
print dict1
thelist = ["5", "6", "7", "2"]
for j in thelist:
	dict1[j:] += 1
print(dict1)

# print(len(thelist))
# for i in thelist:
# 	print(i)
# 	if (i < 3):
# 		thelist.remove(i)
# 		print(str(i) + " removed")
# print(len(thelist))
# print(thelist)

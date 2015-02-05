import numpy as np

thelist = np.random.randint(10, size=10)

for x in range(len(thelist)):
	j = x + 1
	for j in range(x + 1, len(thelist)):
		print("x = " + str(x))
		print("j = " + str(j))
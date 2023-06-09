# importing libraries
import numpy as np

input = np.loadtxt('input1.txt')

i = 1
for value1 in input :
	for value2 in input[i:] :
		j = i + 1
		
		if value1 + value2 == 2020: 
			print(value1, value2, value1*value2)
		
		elif value1 + value2 < 2020:
			for value3 in input[j:] :
				if value1 + value2 + value3 == 2020:
					print(value1, value2, value3, value1*value2*value3)
					print(i, j)

				j += 1		
	i += 1

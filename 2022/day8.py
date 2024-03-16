import numpy as np
data = open("input.txt")

matrix = []
for line in data.readlines():
	row = [int(i) for i in line[:-1]]
	matrix.append(np.array(row))
	
matrix = np.array(matrix)


# PART 1
answer1 = 2 * (len(matrix) + len(matrix[0])) - 4

west = np.zeros_like(matrix)
east = np.zeros_like(matrix)
west[:,0] = matrix[:,0]
east[:,0] = matrix.max(1)

for col in range(1,len(matrix[0])):
	west[:,col] = matrix[:,0:col+1].max(1)
	east[:,col] = matrix[:,col:].max(1)

print(


north = np.zeros_like(matrix)
south = np.zeros_like(matrix)
north[0] = matrix[0]
south[0] = matrix.max(0)

for row in range(1,len(matrix)):
	north[row] = matrix[0:row+1].max(0)
	south[row] = matrix[row:].max(0)

visible = (matrix >= north)
print(matrix)
print(visible)

print(f"Advent of Code, day 1\nAnswer 1: {answer1}")


# PART 2
answer2 = 0

print(f"Answer 2: {answer2}")

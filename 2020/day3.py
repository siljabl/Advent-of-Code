input = open("input3.txt")
rows = input.read().split()

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(f" Slope    # trees")

si = 0
result = 1
for slope in slopes :
	right, down = slope[0], slope[1]
	path = []
	i = 0
	for row in rows[0:len(rows):down] :
		path.append(row[i])
		i = (i + right) % len(row)
	
	trees = path.count('#')
	print(f"{si:4.0f} {trees:10.0f}")
	
	result *= trees
	si += 1
	
print(f"Part 2: {result}")

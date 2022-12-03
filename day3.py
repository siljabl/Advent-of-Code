rugsacks = open("input.txt")
rugsacks = rugsacks.read().split()

# PART 1
lower_code = 96
upper_code = 38

prioritySum = 0
for rugsack in rugsacks:
	div = int( len(rugsack) / 2 )
	comp1 = set(rugsack[:div])
	comp2 = set(rugsack[div:])
	
	item = list(comp1.intersection(comp2))[0]
	if item.islower():
		priority = ord(item) - lower_code
	else:
		priority = ord(item) - upper_code
	
	prioritySum += priority

print(f"Advent of Code 2022\nAnswer 1: {prioritySum}")


# PART 2
prioritySum = 0
for i in range(1,len(rugsacks),3):
	rs1 = set(rugsacks[i-1])
	rs2 = set(rugsacks[i])
	rs3 = set(rugsacks[i+1])
	
	item = list( rs1.intersection(rs2).intersection(rs3) )[0]
	if item.islower():
		priority = ord(item) - lower_code
	else:
		priority = ord(item) - upper_code
	
	prioritySum += priority
	
print(f"Answer 2: {prioritySum}")	

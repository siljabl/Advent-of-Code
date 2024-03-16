import numpy as np
data = open("input.txt")
data = [i for i in data.read()]

# PART 1
for i in range(4, len(data)):
	if len(np.unique(data[i-4:i])) == 4:
		answer1 = i
		break

print(f"Advent of Code, day 1\nAnswer 1: {answer1}")


# PART 1
for i in range(14, len(data)):
	if len(np.unique(data[i-14:i])) == 14:
		answer2 = i
		break

print(f"Answer 2: {answer2}")

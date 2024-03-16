import numpy as np
data = open("input.txt")

data = data.read().split()
data_sorted = np.zeros([4, len(data)])


# PART 1
i = 0
for pair in data:
	pair = pair.split(",")
	elf1 = pair[0].split("-")
	elf2 = pair[1].split("-")

	# min1, min2, max1, max2
	data_sorted[:,i] = elf1[0], elf2[0], elf1[1], elf2[1]
	i += 1
	
min_mask = np.sign(data_sorted[1] - data_sorted[0])   # 1 if elf1 < elf2 
max_mask = np.sign(data_sorted[2] - data_sorted[3])   # 1 if elf1 > elf2

answer1 = (min_mask * max_mask > -1).sum()
print(f"Advent of Code 2022\nAnswer 1: {answer1}")


# PART 2

min_mask = np.sign(data_sorted[2] - data_sorted[1])
max_mask = np.sign(data_sorted[3] - data_sorted[0])

answer2 = (min_mask * max_mask > -1).sum()
print(f"Answer 2: {answer2}")



import numpy as np
data = open("input.txt")
data = data.read().split("\n\n")

init = data[0]
cmds_raw = data[1].split()
cmds_raw = [int(i) for i in cmds_raw[1:len(cmds_raw):2]]

n_crates = int( (len(init.split("\n")[0]) + 1) / 4 )
n_moves = int( len(cmds_raw) / 3 )

crates = [[] for i in range(n_crates)]

cmds = np.zeros([n_crates, n_moves])
for i in range(n_moves):
	val = cmds_raw[0 + 3*i]
	neg = cmds_raw[1 + 3*i]
	pos = cmds_raw[2 + 3*i]
	print(i, val, pos, neg)
	
	cmds[pos-1, i] = val
	cmds[neg-1, i] = -val

print(cmds)

# PART 1
answer1 = 0

print(f"Advent of Code, day 1\nAnswer 1: {answer1}")


# PART 2
answer2 = 0

print(f"Answer 2: {answer2}")

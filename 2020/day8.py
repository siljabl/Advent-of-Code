input = open("input8.txt")
game = input.read().split("\n")

visited = [0 for i in range(len(game)-2)]

idx, itr = 0, 1
acc = 0
while itr <= len(visited) :
	instruction = game[idx].split()
	visited[idx] += itr
	if visited[idx] > itr :
		break
	
	if instruction[0] == "acc" :
		acc += int(instruction[1])
		idx += 1
	
	elif instruction[0] == "jmp" :
		idx += int(instruction[1])
	
	elif instruction[0] == "nop" :
		idx += 1
		
	itr += 1

print(f"Part 1:\nNumbers accumulated after one round is {acc}")



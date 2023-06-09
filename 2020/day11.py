import numpy as np
input = open("input11.txt")
input = input.read().split()

seats = np.zeros([len(input), len(input[0])])
seat_to_num = {'L': -1, '#': 1, '.': 0}

for i in range(len(input)) :
	row = list(input[i])
	row = [seat_to_num[seat] for seat in row]
	seats[i] = np.array(row)


def adjacent_sum(seats) :
	seats = np.pad(seats, 1, 'constant') 
	seats[seats < 0] = 0
	
	adj_sum = -seats
	shifts = [-1, 0, 1]
	for x in shifts :
		for y in shifts :
			adj_sum += np.roll(seats, (x,y), (0,1))
			
	return adj_sum[1:-1,1:-1]

	 
seats_update = seats
converged = sum(sum(np.ones_like(seats)))


rounds = 0
while converged > 0  :
	seats = np.copy(seats_update)
	adjacent = adjacent_sum(seats)
	seats_update[(adjacent == 0) * (seats != 0)] = 1
	seats_update[(adjacent >= 4) * (seats != 0)] = -1
	
	converged = sum(sum(seats_update != seats))
	rounds += 1

	
print(f"Part 1: {sum(seats[seats > 0])}")
	

input = open("input5.txt")
seats = input.read().split()


F, B = 0, 1
row_max, col_max = 127, 7

ID = []
ID_max = 0

def convert(x) :
	if x == "F": return 0
	elif x == "B": return 1
	elif x == "L": return 0
	elif x == "R": return 1


for seat in seats :
	row_low, row_high = 0, row_max
	col_low, col_high = 0, col_max
	
	for ir in range(7) :
		x = convert(seat[ir])
		half = int((row_high - row_low + 1) / 2)
		row_low, row_high = row_low + half*x, row_high - half*(1-x)
	
	for ic in range(7,10) :
		y = convert(seat[ic])
		half = int((col_high - col_low + 1) / 2)
		col_low, col_high = col_low + half*y, col_high - half*(1-y)

			
	ID.append(row_high * 8 + col_high)
	
ID_max = max(ID)		
print(f"Part 1:\nThe highest seat ID: {ID_max}\n")


ID = sorted(ID)
ID_diff = [ID[i+1] - ID[i] for i in range(len(ID)-1)]

for i in range(len(ID_diff)) :
	if ID_diff[i] == 2 :
		break

ID_missing = ID[i] + 1
print(f"Part 2:\nThe missing ID: {ID_missing}")

	
	



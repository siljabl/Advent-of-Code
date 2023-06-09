input = open("input9.txt")
data = input.read().split()
data = [int(i) for i in data]


for i in range(25, len(data)) :
	prev25 = set(data[i-25:i])
	diff = [abs(data[j] - data[i]) for j in range(i-25,i)]
	diff = set(diff)
	
	if prev25 & diff == set() :
		invalid = data[i]
		break
		
print(f"Part 1:\nFirst invalid number : {invalid}\n")


found_seq = False
data_sum = data
len_seq = 1

while not found_seq :
	data_sum = [data_sum[i] + data[i+len_seq] for i in range(len(data)-len_seq)]
	len_seq += 1
	
	if invalid in data_sum :
		found_seq = True
		

idx = data_sum.index(invalid)
seq = data[idx:idx+len_seq]

print(f"Part 2:\nEncryption weakness: {min(seq)+max(seq)}\n")



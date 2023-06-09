input = open("input2.txt")
data = input.read().split()

rules = data[0:len(data):3]
letter = data[1:len(data):3]
codes = data[2:len(data):3]


i, count1, count2 = 0, 0, 0
for code in codes :
	reps = code.count(letter[i][0])
	rule1, rule2 = rules[i].split('-')
	rule1, rule2 = int(rule1), int(rule2)
	
	if reps >= rule1 and reps <= rule2 :
		count1 += 1
	
	if code[rule1-1] == letter[i][0] and code[rule2-1] != letter[i][0] :
		count2 += 1
		
	elif code[rule1-1] != letter[i][0] and code[rule2-1] == letter[i][0] :
		count2 += 1
		
	i += 1

print(f'Part 1:\n{count1} passwords are valid\n')
print(f'Part 2:\n{count2} passwords are valid\n')



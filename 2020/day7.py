input = open("input7.txt")
rules = input.read().split("\n")
rules = rules[:-2]

# sorting data
nuance, color = [], []
bags = []
for rule in rules :
	rule = rule.split()
	nuance.append(rule[0])
	color.append(rule[1])
	bags.append(rule[0] + " " + rule[1])


contained = []
contained_by = []
ibag = 0

for rule in rules :
	rule = rule.split()
	contain = []
	for i in range(2,len(rule)) :
		if rule[i] in nuance and rule[i+1] in color :
			bag = rule[i] + " " + rule[i+1]
			contain.append(bag)
			
	contained.append(contain)
	ibag += 1
	

contained_by = [set() for bag in bags]

for i in range(len(bags)) :
	for bag in contained[i]:
		j = bags.index(bag)
		contained_by[j].add(bags[i])


contains_gold = contained_by[bags.index("shiny gold")]
converged = 0

while converged < len(contains_gold) :
	converged = 0
	for bag in contains_gold :
		add_bags = contained_by[bags.index(bag)]
		if add_bags < contains_gold :
			converged += 1
		else :
			contains_gold = contains_gold|add_bags


print(f"Part 1:\n{len(contains_gold)} bags contains shiny golden bags\n")


in_gold = contained[bags.index("shiny gold")]
print(in_gold)

converged = 0
while converged < len(in_gold) :
	converged = 0
	for bag in in_gold :
		add_bags = set(contained[bags.index(bag)])
		if add_bags < in_gold :
			converged += 1
		else :
			in_gold = in_gold|add_bags

# also needs number...
	




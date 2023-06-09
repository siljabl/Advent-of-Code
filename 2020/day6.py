input = open("input6.txt")
groups = input.read().split("\n\n")

any_sum, all_sum = 0, 0
for group in groups :
	group_any = set(group)
	group_any.discard('\n')
	any_sum += len(group_any)
	
	group_all = group.split()
	if len(group_all) > 1 :
		group_all = [set(group) for group in group_all]
		all_sum += len(set.intersection(*group_all))
	elif len(group_all) == 1 :
		all_sum += len(set(group_all[0]))

print(f"Part 1:\nSum of any counts: {any_sum}\n")
print(f"Part 2:\nSum of all counts: {all_sum}\n")


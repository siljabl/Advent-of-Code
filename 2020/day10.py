input = open("input10.txt")
adapters = input.read().split()
adapters = [int(i) for i in adapters]

adapters = [0] + sorted(adapters) + [max(adapters) + 3]
volt_diff = [adapters[i] - adapters[i-1] for i in range(1,len(adapters))]

diff1 = volt_diff.count(1)
diff3 = volt_diff.count(3)

print(f"Part 1: {diff1*diff3}")

mask1 = [(diff == 1) for diff in volt_diff]
count_comb = 1
print(mask1)


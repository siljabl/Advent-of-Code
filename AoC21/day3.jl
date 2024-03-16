using DelimitedFiles

# Function of base conversion
function convert_base(d, base=10)
   s = zero(eltype(d))
   for val in collect(d)
      s = s * base + val
   end
   return s
end

function problem2(input, operator="most")
	temp = input
	mask = (temp .== input)
	lim = sum(mask) / 2
	output = 0

	for i in 1:len
		temp = temp[mask]
		if length(temp) == 1
			output += temp[1]
			break 
		end

		# count
		count = sum(temp .>= 10^(len-i))
		if operator == "most"
			val = (count >= lim)
		elseif operator == "least"
			val = (count < lim)
		end

		# update
		mask = (div.(temp, 10^(len-i)) .== val)
		lim = sum(mask) / 2
		temp .-= 10^(len-i) * val

		# output
		output += 10^(len-i) * val
	end

	return output
end


# PROBLEM 1
# Import and split
values = readdlm("input/input3.txt", Int)
len = 12

# Preparing
temp = values
lim = length(values) / 2
count = zeros(len)

# Counting
for i in 1:len
	global temp 
	count[end+1-i] = sum(temp .% 10)
	temp = div.(temp, 10)
end

most = (count .>= lim)
least = (count .< lim)

gamma = convert_base(most, 2)
eps = convert_base(least, 2)

answer1 = gamma * eps
println("Problem 1: ")
println(answer1)


# PROBLEM 2
most = problem2(values, "most")
most = [parse(Int, ss) for ss in collect(string(most))]
oxygen = convert_base(most, 2)


least = problem2(values, "least")
least = [parse(Int, ss) for ss in collect(string(least))]
CO2 = convert_base(least, 2)

answer2 = oxygen * CO2
println("\nProblem 2: ")
println(answer2)

using DelimitedFiles

# PROBLEM 1
# Import
input = open(readdlm,"input/input2.txt")
dir = input[1:end, 1]
val = input[1:end, 2]

# Sort
d_step = (dir .== "down") -(dir .== "up")
h_step = (dir .== "forward")

# Compute answer
depth = sum(val .* d_step)
horisontal = sum(val .* h_step)
answer1 = depth * horisontal

# Print
println("Problem 1: ")
println(answer1)


# PROBLEM 2
aim = 0
depth = 0
for i in 1:length(dir)
	global aim, depth

	aim += d_step[i] * val[i]
	depth += aim * h_step[i] * val[i]
end

answer2 = depth * horisontal
println("\nProblem 2: ")
println(answer2)

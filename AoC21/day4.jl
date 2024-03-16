using DelimitedFiles
using LinearAlgebra

n = 5

# PROBLEM 1
# Import
input = open("input/input4.txt")
lines = readlines(input)

draws = split(lines[1], ",")
draws = parse.(Int, draws)

N = Int((length(lines)-1) / (n + 1))
global boards = zeros(N, n, n)
global order = zeros(N, n, n)

# create boards
b = 0
for line in lines[2:end]
    if line == ""
   	 	global i = 1
   	 	global b += 1
   		continue
    end
   
   	boards[b, i, 1:end] = parse.(Int, split(line))
   	i += 1  
end

i = 1
for draw in draws
	order[findall(boards -> boards == draw, boards)] .= i
	global i += 1
end

max_row = maximum(order, dims=2)
max_col = maximum(order, dims=3)

min_row = minimum(max_row)
min_col = minimum(max_col)

# boolian array of winner boards
if min_row < min_col
	global min_val = Int(min_row)
	global min_board = sum((max_row .== min_row), dims=2)
else
	global min_val = Int(min_col)
	global min_board = sum((max_col .== min_col), dims=2)
end

# winner board
board = boards .* min_board

called = draws[min_val]

Sum = 0
for draw in draws[min_val+1:end]
	if draw in board
		global Sum += draw
	end
end

answer1 = called * Sum
println("Problem 1: ")
println(answer1)


# PROBLEM 2
min_row = minimum(max_row, dims=3)
min_col = minimum(max_col, dims=2)

global reached_goal = zeros(N)
for i in 1:N
	reached_goal[i] = min(min_row[i], min_col[i])
end
max_val = Int(maximum(reached_goal))

max_board = (reached_goal .== max_val)

# winner board
board = boards .* max_board

called = draws[max_val]

Sum = 0
for draw in draws[max_val+1:end]
	if draw in board
		global Sum += draw
	end
end

answer2 = Sum * called
println("\nProblem 2: ")
println(answer2)

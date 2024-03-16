using DelimitedFiles

# Problem 1
prev_values = open(readdlm,"input/input1.txt")
values = circshift(prev_values, -1)

diff = (values - prev_values)[1:end-1]
sign = (diff .> 0)
answer1 = sum(sign)

println("Problem 1: ")
println(answer1)


# Problem 2
meas1 = prev_values
meas2 = values
meas3 = circshift(prev_values, -2)

sum_meas = (meas1 + meas2 + meas3)[1:end-2]
sum_meas_next = circshift(sum_meas, -1)

diff = (sum_meas_next - sum_meas)[1:end-1]
sign = (diff .> 0)
answer2 = sum(sign)

println("\nProblem 2: ")
println(answer2)

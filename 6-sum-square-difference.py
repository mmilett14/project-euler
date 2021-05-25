total_sum_squares = 0
for i in range (1, 101):
    total_sum_squares = total_sum_squares + (i*i)

total_squares_sum = 0
for i in range (1, 101):
    total_squares_sum = total_squares_sum + i
total_squares_sum = total_squares_sum * total_squares_sum

print(total_squares_sum - total_sum_squares)

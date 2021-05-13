nums = [1, 2]
i = 0
even_sum = 2
new_sum = 0

while new_num < 4000000:
    new_num = nums[i] + nums[i+1]
    nums.append(new_num)
    i = i + 1

    if new_num % 2 == 0:
        even_sum = even_sum + new_sum

print(even_sum)
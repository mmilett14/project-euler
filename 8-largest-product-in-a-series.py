# Use sliding Window

# Solved problem
window_max = 0
i = 0

for i in range(0, len(num)-12):
    window_prod = int(num[i]) * int(num[i+1]) * int(num[i+2]) * int(num[i+3]) * int(num[i+4]) * int(num[i+5]) * int(num[i+6]) * int(num[i+7]) * int(num[i+8]) * int(num[i+9]) * int(num[i+10]) * int(num[i+11]) * int(num[i+12])

    if window_prod > window_max:
        window_max = window_prod

print(window_max)

# Use sliding Window

# Solved first part of problem
window_max = 0
i = 0

for i in range(0, len(num)-3):
    window_prod = int(num[i]) * int(num[i+1]) * int(num[i+2]) * int(num[i+3])

    if window_prod > window_max:
        window_max = window_prod

print(window_max)

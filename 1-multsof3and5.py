running_total = 0

for i in range(0,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        running_total = running_total + i
print(running_total)
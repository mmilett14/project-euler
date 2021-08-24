import math

int_dict = {i: True for i in range(2, 10)}

## Need to create a constant j variable

for i in range(2, round(math.sqrt(9+1))):
    if int_dict[i] == True:
        j = i**2
        multiplier = 1
        int_dict[j] = False
        for j in range(j, 9):
            j = j+(i*multiplier)
            int_dict[j] = False
            multiplier += 1

print(int_dict)

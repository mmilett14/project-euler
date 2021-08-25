import math

def prime(n):
    int_dict = {i: True for i in range(2, n+1)}

    for i in range(2, round(math.sqrt(n))):
        if int_dict[i] == True:
            j = i**2
            multiplier = 1
            int_dict[j] = False

            j_dynamic = j

            while j_dynamic < n-1:
                j_dynamic = j+(i*multiplier)
                int_dict[j_dynamic] = False
                multiplier += 1
    
    # need to return the 10,001st prime, not just dictionary
    print(int_dict)

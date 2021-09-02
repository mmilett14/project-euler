from math import sqrt, ceil, log

# from https://codereview.stackexchange.com/questions/188053/project-euler-problem-7-in-python-10001st-prime-number
def upper_bound(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def prime(n):
    
    top_range = upper_bound(n)
    
    int_dict = {i: True for i in range(2, top_range)}

    for i in range(2, round(sqrt(top_range))):
        if int_dict[i] == True:
            j = i**2
            multiplier = 1
            int_dict[j] = False

            j_dynamic = j

            while j_dynamic < top_range-1:
                j_dynamic = j+(i*multiplier)
                int_dict[j_dynamic] = False
                multiplier += 1

    prime_list = []
    
    while len(prime_list) <= n:
        for key, value in int_dict.items():
            if value == True:
                prime_list.append(key)
            
    print(prime_list[-1])
    


from math, import sqrt, ceil, log

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
    prime_list = []
    
    for key, value in int_dict.items():
        if value == True:
            prime_list.append(key)
            
    print(prime_list[-1])
    
# from https://codereview.stackexchange.com/questions/188053/project-euler-problem-7-in-python-10001st-prime-number
def upper_bound(n):
if n < 6:
    return 100
return ceil(n * (log(n) + log(log(n))))

# Solved first part of problem using Sieve of Eratosthenes.
marked = []
prime = []

for i in range (2,14):
    if i not in marked:
        prime.append(i)

        for j in range (2, 14):
            marked.append(i*j)

print(prime)

# Need to solve second part of problem using Trial Division.

### This needs work.

num_list = [2]

prime = [2]

i = 2

while len(prime) < 10:
    i = i + 1
    
    
    for num in num_list:
        if i % num != 0:
            prime.append(i)
            print(prime)
    
    num_list.append(i)

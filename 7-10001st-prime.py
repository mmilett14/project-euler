# Implement Sieve of Eratosthenes.

# Solved first part of problem.
marked = []
prime = []

for i in range (2,14):
    if i not in marked:
        prime.append(i)

        for j in range (2, 14):
            marked.append(i*j)

print(prime)

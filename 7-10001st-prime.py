marked = []
prime = []

while len(prime) < 10002:
    for i in range (2,1000000):
        if i not in marked:
            prime.append(i)
            for j in range (2, 1000000):
                marked.append(i*j)

print(prime[-1])

import math

lrg_prime = 1

euler = 600851475143

for i in range (1, math.sqrt(euler)):
    if euler % i == 0:
        lrg_prime = i
        print(lrg_prime)

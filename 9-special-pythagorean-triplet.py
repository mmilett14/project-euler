# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 1
b = 2
c = 3
add = a + b + c

while add < 1000:
    if a^2 + b^2 == c^2:
        if add == 1000:
            print(a, b, c)
    a += 1
    b += 2
    c += 3
    add = a + b + c
    print(add)
    

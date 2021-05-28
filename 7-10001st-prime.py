num_list = [2]

prime = [2]

i = 2

while len(prime) < 10002:
    i = i + 1

    for num in num_list:
        if i % num == 0:
            break
        else:
            if i not in prime:
                prime.append(i)
    
    if i not in num_list:
        num_list.append(i)

print(prime[-1])

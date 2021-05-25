dict_num = {}

for i in range (100,1000):

    for j in range (100,1000):
        prod = i * j

        if prod not in dict_num:
            dict_num[prod] = prod

for key in dict_num:
    dict_num[key] = str(key)

dict_rev = {}
big_match = 0
for key in dict_num:
    dict_num[key] = list(dict_num[key])
    dict_rev[key] = list(reversed((dict_num[key])))

    if dict_num[key] == dict_rev[key]:
        new_int = ''.join(dict_rev[key])
        new_int = int(new_int)
        big_match.append(new_int)
        
print(max(big_match))

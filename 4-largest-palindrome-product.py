dict_num = {}

for i in range (100,1000):

    for j in range (100,1000):
        prod = i * j

        if prod not in dict_num:
            dict_num[prod] = prod

#print(dict_num)


for key in dict_num:
    dict_num[key] = str(key)

#print(dict_num)

dict_rev = {}

big_match = 0

for key in dict_num:
    dict_num[key] = list(dict_num[key])
    dict_rev[key] = list(reversed((dict_num[key])))

    if dict_num[key] == dict_rev[key]:
        big_match = dict_num[key]
        print(big_match)

### Need to convert back to integer to find biggest number.

print(big_match)
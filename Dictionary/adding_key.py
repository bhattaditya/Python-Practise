# dictionaries are mutables --> can be changed

d1= {0: 10, 1: 20}

print(d1)

d1[0] = "changed"
d1[1] = "changed"

print(d1)
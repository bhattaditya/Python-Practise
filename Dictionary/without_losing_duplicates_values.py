l1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
l2 = [1, 2, 2, 3]

d = {}

for key, value in zip(l1, l2):
    d[key] = value

print(d)    
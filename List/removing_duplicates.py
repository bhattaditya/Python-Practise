l1 = [10, 50, 90, 30, 20, 20 ,10, 50, 30, 90]

print(list(set(l1)))

print(l1)
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)        
from collections import Counter

d =  {'item1': 45, 'item2':35, 'item3': 41, 'item4':55, 'item5': 24}

for i in d.items():
    print(i)

p = Counter(d)

print(p.most_common(3))


"""key values sorting"""

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

for key, value in num.items():
    print(key, sorted(value))

print()

d = {key: sorted(value) for key, value in num.items()}

print(d)
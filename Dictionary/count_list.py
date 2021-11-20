d = {'k1': [10, 20, 40], 'k2': [50]}


for key, value in d.items():
    print(f'{key} has {len(value)} items')


print('All items values count: ', sum(map(len, d.values())))


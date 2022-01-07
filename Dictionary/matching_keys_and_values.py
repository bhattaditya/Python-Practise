d1 = {'key1': 1, 'key2': 2, 'key3': 2}
d2 = {'key1': 1, 'key2': 2, 'key4': 5}

for i in d1.items():
    if i in d2.items():
        print(*i)
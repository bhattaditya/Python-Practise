d = {'k1': 10, 'k2': 20, 'k3': 40}

for i in d.items():
    print(i)

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}

for name, details in students.items():
    print(name)
    for d1, d2 in details.items():
        print(d1, d2)
    print()
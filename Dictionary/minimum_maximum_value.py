d1 = {
    "key100": 50,
    "key300": 20,
    "key500": 100,
    "key400": 10,
    "key200": 30,
}

mi = sorted(d1.values())[0]
ma = sorted(d1.values())[-1]

print(f'Minimun: {mi}  and Maximum: {ma}')

# or do this
print()
print("Maximum:", max(d1.values()))
print("Minimum:", min(d1.values()))


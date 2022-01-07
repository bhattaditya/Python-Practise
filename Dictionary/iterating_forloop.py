d1 = {
    "key100": 50,
    "key300": 20,
    "key500": 100,
    "key400": 10,
    "key200": 30,
}

# iterating over both keys and values as items() returns the key: value pairs as tuples
for key, value in d1.items():
    print(key, value)

print()
# iterating over keys only
for item in d1:
    print(item)   

print()
# iterating over values only
for value in d1.values():
    print(value)

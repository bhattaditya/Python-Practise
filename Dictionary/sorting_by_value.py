import operator
d1 = {
    "key100": 50,
    "key300": 20,
    "key500": 100,
    "key400": 10,
    "key200": 30,
}

print(d1)
print(sorted(d1.values()))
print(sorted(d1.values(), reverse=True))
print("sorting by value -> ", dict(sorted(d1.items(), key=operator.itemgetter(1))))
print("sorting by key -> ", dict(sorted(d1.items(), key=operator.itemgetter(0))))
print("by defalut sorting by key -> ", dict(sorted(d1.items())))
print(dict(sorted(d1.items(), key=operator.itemgetter(1),reverse=True)))
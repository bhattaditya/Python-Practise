import operator

l =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l = []

# simple sorting 
print(sorted(l))

print(sorted(l, key=operator.itemgetter(0)))

# sorting using key
print(sorted(l, key=operator.itemgetter(1)))



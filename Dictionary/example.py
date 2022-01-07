from collections import Counter, defaultdict
from operator import itemgetter


def collectionfunc(text1, dictionary1, deduct, list1, val1, key1):
    # Write your code here
    c = Counter(text1.split(" "))
    d = dict(c)
    print(dict(sorted(d.items(), key=itemgetter(0))))
    
    d2 =  Counter(deduct) - Counter(dictionary1)
    print(dict(d2))

    d3 = dict(zip(key1,val1))
    del d3[key1[1]]
    d3[key1[1]] = val1[1]
    print(d3)

    d3 = {'odd': [], 'even': []}
    
    print({'odd':[i] for i in list1 if i%2 !=0})

    for i in list1:
        if i % 2 ==0:
            d3['even'].append(i)
        if i % 2 !=0:
            d3['odd'].append(i)

    print(d3)

    d4 = defaultdict()

text1 = "how many times does each word show up in this sentence word times each each word"
dictionary1 = {'11': 33, '42': 14, '12': 16, '45': 34, '81': 64}
deduct = {'33': 5, '11': 6, '42': 4}
list1 = [1,2,3,4,5,6,7,10]
val1 = [1,2,3]
key1 = ['a', 'b', 'c']
collectionfunc(text1, dictionary1, deduct, list1, val1, key1)

   


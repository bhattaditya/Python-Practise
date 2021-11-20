from collections import Counter

item_list = [
            {'item': 'item1', 'amount': 400}, 
            {'item': 'item2', 'amount': 300}, 
            {'item': 'item1', 'amount': 750}
        ]

result = Counter()
r = {}

for d in item_list:
    result[d['item']] += d['amount']

# dict will convert back the Counter object to dictionary
print(dict(result))



    



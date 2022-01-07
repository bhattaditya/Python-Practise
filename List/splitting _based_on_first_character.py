from itertools import groupby
import operator

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

word_dict = {}
l = []

# for word in word_list:
#     key = word[0]

#     for w in word_list:
#         if w.startswith(key):
#             if w not in l:
#                 l.append(w)
#     # word_dict[key]
    

# print(l)

for letter, word in groupby(sorted(word_list), key = operator.itemgetter(0)):
    print(letter, ' - ')
    for w in word:
        print(w)
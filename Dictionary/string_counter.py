from collections import Counter

s = 'w3resource'
s1 = Counter(s)
s2 = ''.join(set(list(s)))
count = 0
d = {}

for i in s1:
    d[i] = s.count(i)
    count = 0

print(d)    

# or this method

str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter + 0) + 1 
    # my_dict[letter] = my_dict.get(letter + 1) 
print(my_dict)



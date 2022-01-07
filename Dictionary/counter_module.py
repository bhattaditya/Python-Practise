from collections import Counter
 
# Initial Dictionary
my_dict = {'G': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}
 
k = Counter(my_dict)
 
# Finding 3 highest values
high = k.most_common(3)
 
print("Initial Dictionary:")
print(my_dict, "\n")
 
 
print("Dictionary with 3 highest values:")
print("Keys: Values")
 
for i in high:
    print(i[0]," :",i[1]," ")


# 2nd example

d = {'Math':81, 'Physics':83, 'Chemistry':87}
print(Counter(d).most_common())
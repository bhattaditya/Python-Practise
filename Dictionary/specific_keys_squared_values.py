# finding x: x*x values in range of 1-15 both included
d1 = {
    1: 1,
    2: 4, 
    3: 9,
    4: 16,
    5: 25, 
    6: 36, 
    7: 49, 
    8: 64, 
    9: 81, 
    10: 100, 
    11: 121, 
    12: 144, 
    13: 169, 
    14: 196, 
    15: 225,
    16: 256,
    17: 289,
}

d2 = {}  # empty dictionary for storing filtered key:value pairs

for key, value in d1.items():
    if 1 <= key <= 15 and value == key * key:
        d2[key] = value

# using comphrehension
d3 = {key:value for key, value in d1.items() if 1<= key<=15 and value == key * key}

print(d2)        
print(d3)





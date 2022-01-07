def common1(l1, l2) -> list:
    l3 = []

    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

def common2(l1, l2):
    l3 = [i for i in l1 if i in l2]
    return l3

l1 = [10, 20, 30] 
l2 = [10, 50, 60, 70, 20]

common_items1 = common1(l1, l2)
common_items2 = common2(l1, l2)

print(common_items1)
print(common_items2)
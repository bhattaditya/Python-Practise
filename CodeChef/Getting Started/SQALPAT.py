n = int(input('>: '))

s = 0

for i in range(1,n+1):
    for j in range(5):
        if i%2!=0:
            s += 1
            print(s, end=' ')
        else:
            print(i*5-j, end=' ')
            s += 1
    print()
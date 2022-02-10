# cook your dish here
t = int(input())
for _ in range(t):
    num = int(input())
    zeros = 0
    count = 0
    d = 5
    
    while num//d:
        count += num//d
        d *= 5
    print(count)
# cook your dish here
t = int(input())

for _ in range(t):
    num = int(input())
    cars = list(map(int, input().split()))
    minimum_speed = cars[0]
    count = 1
    
    for i in range(1, num):
        if cars[i]<= minimum_speed:
            count += 1
        if cars[i]< minimum_speed:
            minimum_speed = cars[i]
    print(count)
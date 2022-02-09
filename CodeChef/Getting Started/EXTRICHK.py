a, b, c = map(int, input().split())

if a+b>c and b+c>a and c+a>b:
    if a==b==c:
        # equilateral
        print(1)
    elif a==b or b==c or c==a:
        # ssosceles 
        print(2)
    else:
        # scalene 
        print(3)
else:
    # not triangle
    print(-1)
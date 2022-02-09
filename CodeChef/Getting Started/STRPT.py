n = int(input(">: "))

# left triangle
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

# right triangle
for i in range(n):
    for space in range(n-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()


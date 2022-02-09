# cook your dish here
t = int(input())

for i in range(t):
    s = input()
    mid = len(s)//2
    
    if len(s)%2 == 0:
        first_half = s[:mid]    
        second_half = s[mid:]
    else:
        first_half = s[:mid]    
        second_half = s[mid+1:]

    if sorted(first_half) == sorted(second_half):
        print('YES')
    else:
        print('NO')

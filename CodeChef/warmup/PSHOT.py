# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    penalty_shoots = input()
    s = 2 * n
    
    current_score_A = 0
    current_score_B = 0
    left_A_shoots = n
    left_B_shoots = n
    result = s
    
    for i in range(s):
        if i%2 == 0:
            if penalty_shoots[i] == '1':
                current_score_A += 1
                left_A_shoots -= 1
            else:
                # A shoot missed
                left_A_shoots -= 1
        else:
            if penalty_shoots[i] == '1':
                current_score_B += 1
                left_B_shoots -= 1
            else:
                # B shoot missed
                left_B_shoots -= 1
        
        if current_score_A > (current_score_B + left_B_shoots):
            result = i + 1
            break
        elif current_score_B > (current_score_A + left_A_shoots):
            result = i + 1
            break
    print(result)

print('A left shoots: ', left_A_shoots)
print('B left shoots: ', left_B_shoots)
print(penalty_shoots)
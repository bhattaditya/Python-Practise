t = int(input())

for _ in range(t):
    games_played = int(input())
    for _ in range(games_played):
        initial_state, rounds, guess = map(int, input().split()) # 1 or 2
        count = rounds//2
        
        if initial_state == 1 and guess == 1 or initial_state == 2 and guess == 2:
            print(count)
        elif initial_state == 1 and guess == 2 or initial_state == 2 and guess ==1:
            print(rounds-count)
            
        # else can be elif
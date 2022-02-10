potential_customers = int(input())
budget = []
mx = 0

for i in range(potential_customers):
    b = int(input())
    budget.append(b)

budget.sort()

for i in range(potential_customers):
    # sprint(budget[i]*(potential_customers-i), end=' ')
    mx = max(mx, budget[i]*(potential_customers-i))
print(mx)

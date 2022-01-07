n = int(input("Enter n to generate n: n * n dictionary "))

# using comphrehensions
d1 = {i:i*i for i in range(1, n+1)}

print(d1)
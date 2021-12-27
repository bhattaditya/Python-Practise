number = int(input("Number: "))
total_sum = 0
i = 0
j = 0
digits = ''

# saving number copy to number1
number1 = number

# converting decimal number to octal 
while number > 0:
    remainder = number % 8
    number = number // 8
    digits += str(remainder)

# reversing digit string to get actual binary string then its converted back to integer
octal_number = int(digits[::-1])

print(f'Octal Number: {octal_number}')

# converting octal to decimal
while octal_number > 0:
    remainder = octal_number % 10
    total_sum += pow(8, j) * remainder
    octal_number = octal_number // 10
    j += 1
    
print(f"Original Number : {total_sum}")

# pythonic way
print(oct(number1).replace('0o', ''))
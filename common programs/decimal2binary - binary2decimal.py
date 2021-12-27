number = int(input("Number: "))
total_sum = 0
i = 0
j = 0
digits = ''

# saving number copy to number1
number1 = number

# converting decimal number to binary 
while number > 0:
    remainder = number % 2
    number = number // 2
    digits += str(remainder)

# reversing digit string to get actual binary string then its converted back to integer
binary_number = int(digits[::-1])

print(f'Binary Number: {binary_number}')

# converting binary to decimal
while binary_number > 0:
    remainder = binary_number % 10
    total_sum += pow(2, j) * remainder
    binary_number = binary_number // 10
    j += 1
    
print(f"Original Number : {total_sum}")

# pythonic way
print(bin(number1).replace('0b', ''))
def is_prime(number):
    if number <= 1:
        return "Not Prime Number"
    elif number == 2 or number == 3:
        return "Prime Number"    
    else:
        for i in range(2, (number//2) + 1):
            if number % i == 0:
               return 'Not a prime no'
        else:
            return 'Prime Number'

if __name__ == "__main__":
    number = int(input("Number: "))
    res = is_prime(number)
    print(res)
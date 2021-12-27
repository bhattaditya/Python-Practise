def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number -1)

if __name__ == "__main__":
    number = int(input("Number: "))
    result = factorial(number)
    print(result)
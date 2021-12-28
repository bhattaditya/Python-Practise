def digit_sum(number):
    sum_digit = 0

    while number > 0:
        digit = number % 10
        number //= 10
        sum_digit +=  digit

    return sum_digit

if __name__ == "__main__":
    number = int(input("Number: "))
    result = digit_sum(number)
    print(result)
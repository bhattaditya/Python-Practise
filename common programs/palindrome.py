def is_palindrome_number(number):
    reversed_num = 0
    number_copy = number

    while number > 0:
        digit = number % 10
        number //= 10
        reversed_num = 10 * reversed_num + digit
        print(number)
    return reversed_num == number_copy

# pythonic way
def is_palindrome_string(string):
    return string == string[::-1]


if __name__ == "__main__":
    number = int(input('Number: '))
    print(is_palindrome_number(number))

    string = input("String: ")
    print(is_palindrome_string(string))

    


def reverse(string):
    
    # splits on spaces i.e word
    string_list = string.split(' ')

    new_string_list = []
    for word in string_list:
        new_string_list.append(word[::-1])

    # joining the reversed word list with space 
    words_reversed = ' '.join(new_string_list)

    return words_reversed


# def reverse(string):
#     return ' '.join([word[::-1] for word in string.split(' ')])

if __name__ == "__main__":
    string = input("String: ")
    print(reverse(string))
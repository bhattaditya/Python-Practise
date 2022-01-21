"""
return a new string made of every other char starting with the first.
"""

def string_bits(str):
    s = ''
    for i in range(0,len(str),2):
        s += str[i]
    return s

if __name__ == "__main__":
    print(string_bits('qwerty'))
    print(string_bits('qqwweerrttyy'))
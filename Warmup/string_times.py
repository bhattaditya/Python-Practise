from unicodedata import name


"""
returns n copies of the string.
"""

def string_times(str, n):
    return str*n

if __name__ == "__main__":
    print(string_times('Repeat', 2))
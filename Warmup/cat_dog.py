"""
Return True if number of 'cat' equals to number of 'dog'
"""

def cat_dog(str):
  return (str.count('cat') == str.count('dog'))


if __name__ == "__main__":
    print(cat_dog('catdogabcefgcatdog.'))
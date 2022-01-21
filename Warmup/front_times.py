"""
Returns n times string first three characters if present.  Else return n times string. 
"""

def front_times(str, n):
  if len(str)<3:
    return str*n
  return str[:3]*n

if __name__ == "__main__":
  print('n times first 3 characters: ',front_times('qwerty', 2))
  print('n times characters: ',front_times('n', 2))
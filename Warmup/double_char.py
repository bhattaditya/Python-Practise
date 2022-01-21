"""
return string with each character doubled.
"""

def double_char(str):
  s = ''
  for i in range(len(str)):
    s += str[i]*2
  return s

if __name__ == "__main__":
    print(double_char('Double'))
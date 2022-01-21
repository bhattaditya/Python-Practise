"""
If a or b have common part in the end irrespective of case.
"""

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a.endswith(b) or b.endswith(a)

if __name__ == "__main__":
    print(end_other('abc', 'abXabc'))
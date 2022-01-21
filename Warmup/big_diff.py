"""
return the difference between the largest and smallest values in the array.
"""

def big_diff(nums):
  return max(nums) - min(nums)

if __name__ == "__main__":
    print(big_diff([10, 3, 5, 6]))
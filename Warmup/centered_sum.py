"""
Return the "centered" average of an array of ints. Ignore largest and smallest element not the copies.
"""

def centered_average(nums):
    nums.sort()
    return ( sum(nums[1:-1]) / (len(nums)-2) )

if __name__ == "__main__":
    print(centered_average([1, 2, 3, 4, 100]))
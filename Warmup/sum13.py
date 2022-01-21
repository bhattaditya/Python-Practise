"""
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""

def sum13(nums):
    s = 0
    index = 0
    while index < len(nums):
        if nums[index] == 13:
            index += 2
            continue
        else:
            s  += nums[index]
        index += 1
    return s

if __name__ == "__main__":
    print(sum13([1, 2, 2, 1, 13])) # 6
    print(sum13([13, 1, 2, 13, 2, 1, 13])) # 3

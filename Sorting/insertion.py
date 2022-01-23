"""
creates a sublist in left and compares the right element with left sub list.

Time - O(n^2)
Space - O(1)
"""

def insertionSort(array):
    for i in range(1, len(array)):
        # i moves towards right
        j = i
        while j > 0 and array[j] < array[j-1]:
            # j moves towards left
            swap(j, j-1, array)
            j -= 1
    return array

def swap(x,y,array):
    array[x], array[y] = array[y], array[x]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sortedArray = insertionSort(arr)
    print(sortedArray)
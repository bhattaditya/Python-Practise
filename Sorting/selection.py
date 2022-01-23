"""
In this sorting algo, left side gets sorted at each ith iteration.

Time - O(n^2)
Space - O(1)
"""

def selectionSort(array):
    for i in range(len(array)-1):
        minimum = i
        # suppose ith element index is minimum value.
        for j in range(i+1, len(array)):
            # compare the (i+1)th element i.e 'j'th with the minimum ekement i.e 'i'th
            if array[minimum] > array[j]:
                minimum = j
        # swaps the minimum value with 'i'th element
        swap(i,minimum,array)
    return array
        
def swap(x, y , array):
    array[x], array[y] = array[y], array[x]

if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    result = selectionSort(array)
    print(result)
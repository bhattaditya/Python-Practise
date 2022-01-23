"""
In this sorting algo, right side gets sorted at each ith iteration.

Time - O(n^2)
Space - O(1)
"""

def bubbleSort(array):
    for i in range(len(array)-1):
        # each iteration will bubble out the maximum number to the right
        # right side will be get sorted 
        for j in range(0,len(array)-i-1):
            # looping to [0-len(array)-i-1] as we are accessing 'j+1' index, thats why '-1'
            # and as right side get sorted at each iteration we can ignore that part, thats why '-i'
            if array[j] > array[j+1]:
                swap(j,j+1, array)

    return array

def swap(x,y,array):
    array[x], array[y] = array[y], array[x]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sortedArray = bubbleSort(arr)
    print(sortedArray)
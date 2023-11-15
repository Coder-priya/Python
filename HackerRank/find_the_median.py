def findMedian(arr):
    # Write your code here
    arr.sort()
    middle_index = len(arr) // 2
    median = arr[middle_index]
    
    return median

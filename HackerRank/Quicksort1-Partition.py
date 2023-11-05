"""
Complete the 'quickSort' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts INTEGER_ARRAY arr as parameter.
"""
def quickSort(arr):
    # Write your code here
    left = [i for i in arr if i < arr[0]]
    right = [i for i in arr if i > arr[0]]
    equal = [i for i in arr if i == arr[0]]
    return left + equal + right

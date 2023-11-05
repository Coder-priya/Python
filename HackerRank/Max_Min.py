# Complete the 'maxMin' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    min_unfairness = float('inf')
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        current_unfairness = subarray[-1] - subarray[0]
        min_unfairness = min(min_unfairness, current_unfairness)

    return min_unfairness

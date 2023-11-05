"""
Complete the 'gamingArray' function below.

The function is expected to return a STRING.
The function accepts INTEGER_ARRAY arr as parameter.
"""
def gamingArray(arr):
    # Write your code here
    count = 0 
    prev = 0
    for num in arr:
        if (num > prev):
            prev = num
            count=count+1
    if(count % 2 == 0):
        return "ANDY"
    else:
        return "BOB"

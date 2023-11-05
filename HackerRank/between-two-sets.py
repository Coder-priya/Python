"""
Complete the 'getTotalX' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
1. INTEGER_ARRAY a
2. INTEGER_ARRAY b
"""

def getTotalX(a, b):
    # Write your code here
    res = 0
    for i in range(max(a), min(b) + 1):
        res += (all([i % aa == 0 for aa in a]) and all([bb % i == 0 for bb in b]))
    return res

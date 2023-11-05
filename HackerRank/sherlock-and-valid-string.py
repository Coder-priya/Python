"""
Complete the 'isValid' function below.

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
"""
def isValid(s):
    # Write your code here
    res = set()
    removed = False
    
    for i in set(s):
        c = s.count(i)

        if res == set():
            res.add(c)
            
        else:
            if len(res) == 1:
                element = next(iter(res))
                if element == 1:
                    if removed:
                        return "NO"
                    removed = True
                    res = {c}
                elif c== 1:
                    if removed:
                        return "NO"
                    removed = True
                elif element - c == -1:
                    if removed:
                        return "NO"
                    removed = True
                elif element - c == 1:
                    if removed:
                        return "NO"
                    removed = True
                    res = {c}
                elif abs(element - c) >= 2:
                    return "NO"

    return "YES" if len(res) == 1 else "NO"

"""
Complete the 'superReducedString' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
"""
def superReducedString(s):
    # Write your code here
    stack=["#"]
    for i in s:
        if stack[-1]==i:    
            stack.pop()     
        else:
            stack.append(i)     
    ans=""
    for i in stack[1:]:     
        ans+=i              
    if ans:
        return ans          
    return "Empty String"

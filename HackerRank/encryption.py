# Complete the 'encryption' function below.

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def encryption(s):
    # Write your code here
    p=''.join(s.split(' '))
    a=list(map(list,p))
    f=''
    col=math.ceil(math.sqrt(len(a)))
    for d in range(col):
        for j in range(d,len(a),col):
            f+=p[j]
        f+=' '
    return f

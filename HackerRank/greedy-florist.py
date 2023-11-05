# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    tCost = 0
    prevPurchase = 0
    for i in range(len(c)):
        tCost += (prevPurchase // k + 1) * c[i]
        prevPurchase += 1

    return tCost

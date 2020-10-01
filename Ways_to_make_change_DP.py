#Time - O(N) / Space - O(N)
def waysforChange(n,denoms):
    ways=[0 for i in range(n+1)]
    ways[0]=1
    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                ways[amount]+=ways[amount-denom]
    return ways[n]
n=8
denoms=[2,4,6]
print(waysforChange(n,denoms))

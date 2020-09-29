#Time - O(N) / Space - O(N)
def getnthFibonacci(n,memoize={1:0,2:1}):
    if n not in memoize:
        memoize[n]=getnthFibonacci(n-1,memoize)+getnthFibonacci(n-2,memoize)
        return memoize[n]
    else:
        return memoize[n]
N=int(input())
print(getnthFibonacci(N))

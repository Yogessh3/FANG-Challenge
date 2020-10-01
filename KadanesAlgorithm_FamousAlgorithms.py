#Time - O(N) / Space - O(1)
def kadanesAlgorithm(array):
    maxReached=array[0]
    maxSoFar=array[0]
    for i in range(1,len(array)):
        maxReached=max(array[i],array[i]+maxReached)
        maxSoFar=max(maxSoFar,maxReached)
    return maxSoFar
array=[-15,-1,9,8,-9,25,6]
print(kadanesAlgorithm(array))

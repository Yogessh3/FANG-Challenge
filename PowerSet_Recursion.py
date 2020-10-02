#Time - O(N*2^N) / Space - O(N*2^N)
def powerSet(array,idx):
    if idx<0:
        return [[]]
    ele=array[idx]
    subsets=powerSet(array,idx-1)
    for i in range(len(subsets)):
        currentSubset=subsets[i]
        subsets.append(currentSubset+[ele])
    return subsets
array=[1,2,3]
idx=len(array)-1
powerset=powerSet(array,idx)
print(*powerset)
            

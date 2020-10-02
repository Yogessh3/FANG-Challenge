#Time - O(N!*N) / Space - O(N!*N)
def getPermutations(array):
    permutations=[]
    permutationsHelper(0,array,permutations)
    return permutations
def permutationsHelper(i,array,permutations):
    if(i==len(array)-1):
        permutations.append(array[:])
    else:
        for j in range(i,len(array)):
            swap(i,j,array)
            permutationsHelper(i+1,array,permutations)
            swap(i,j,array)
def swap(i,j,array):
    array[i],array[j]=array[j],array[i]
array=[1,2,3]
permutation=getPermutations(array)
for i in permutation:
    print(i)


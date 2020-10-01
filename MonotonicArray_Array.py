#Time - O(N) / Space - O(1)
def monotonicArray(array):
    isNonIncreasing=True
    isNonDecreasing=True
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            isNonIncreasing=False
        elif array[i] > array[i+1]:
            isNonDecreasing=False
    return isNonIncreasing or isNonDecreasing
array=[2,3,4,5,4,3]
print(monotonicArray(array))

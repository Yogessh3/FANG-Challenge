def subarraySort(array):
    minOutOfOrder=float("inf")
    maxOutOfOrder=float("-inf")
    for i in range(len(array)):
        num=array[i]
        if(isOutOfOrder(i,num,array)):
            minOutOfOrder=min(num,minOutOfOrder)
            maxOutOfOrder=max(num,maxOutOfOrder)
    if(minOutOfOrder==float("inf")):
        return [-1,-1]
    subarrayLeftIdx=0
    subarrayRightIdx=len(array)-1
    while minOutOfOrder>=array[subarrayLeftIdx]:
        subarrayLeftIdx+=1
    while maxOutOfOrder<=array[subarrayRightIdx]:
        subarrayRightIdx-=1
    return [subarrayLeftIdx,subarrayRightIdx]
def isOutOfOrder(i,num,array):
    if(i==0):
        return num>array[i+1]
    elif(i==len(array)-1):
        return num<array[i-1]
    else:
        return num<array[i-1] or num>array[i+1]
array=[1,2,3,7,8,6,8,7,12]
print(subarraySort(array))
            
        

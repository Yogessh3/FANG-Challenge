#Time - O(N) / Space - O(N)
def largestRange(array):
    bestRange=[]
    longestRange=0
    nums={}
    for num in array:
        nums[num]=True
    for i in range(len(array)):
        num=array[i]
        if nums[num]==False:
            continue
        currentRange=1
        left=num-1
        right=num+1
        while left in nums:
            currentRange+=1
            nums[left]=False
            left-=1
        while right in nums:
            currentRange+=1
            nums[right]=False
            right+=1
        if currentRange > longestRange:
            longestRange=currentRange
            bestRange=[left+1,right-1]
    return bestRange
array=[5,2,3,1,8,9,12,11,10]
print(largestRange(array))
        
        
    

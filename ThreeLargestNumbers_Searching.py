#Time - O(NlogN) (i.e) Sorting / Space - O(1)
import heapq
def findThreeLargestNumbers(array):
    hq=[]
    for num in array:
        if len(hq)<3:
            heapq.heappush(hq,num)
        else:
            if(hq[0]<num):
                heapq.heappop(hq)
                heapq.heappush(hq,num)
    return sorted(hq)
array=[8,-5,6,9,2,3,10,12,11]
print(*findThreeLargestNumbers(array))
                

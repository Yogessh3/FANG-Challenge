def waterArea(heights):
    maxes=[0 for i in range(len(heights))]
    leftMax=0
    for i in range(len(heights)):
        height=heights[i]
        maxes[i]=leftMax
        leftMax=max(leftMax,height)
    rightMax=0
    for i in reversed(range(len(heights))):
        height=heights[i]
        minHeight=min(maxes[i],rightMax)
        if(height<minHeight):
            maxes[i]=minHeight-height
        else:
            maxes[i]=0
        rightMax=max(rightMax,height)
    return maxes
heights=[2,0,0,5,0,8,10]
print(waterArea(heights))
                               
        
        
        

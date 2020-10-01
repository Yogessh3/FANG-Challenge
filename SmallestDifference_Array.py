#Time - O(NlogN + MlogM) / Space - O(1)
def smallestDifference(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne=0
    idxTwo=0
    smallest=float("inf")
    smallNumbers=[]
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum=arrayOne[idxOne]
        secondNum=arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne+=1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo+=1
        else:
            return [firstNum,secondNum]
        if current < smallest:
            smallest = current
            smallNumbers=[firstNum,secondNum]
    return smallNumbers
arrayOne=[60,9,12,3,54,26]
arrayTwo=[23,65,41,28,84,19]
print(smallestDifference(arrayOne,arrayTwo))
        
            

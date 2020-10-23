def findClosestValue(root,key):
    return findClosestHelper(root,float("inf"),key)
def findClosestHelper(root,closestValue,key):
    if root is None:
        return ClosestValue
    if abs(closestValue-root.value) < abs(closestValue-key):
        closestValue=root.value
    if(key<root.value):
        findClosestHelper(root.left,closestValue,key)
    elif(key>root.right):
        findClosestHelper(root.right,closestValue,key)
    else:
        return closest

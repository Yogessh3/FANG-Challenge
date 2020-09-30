#Time O(N) / Space - O(N) (i.e) Recursion Stack
def validateBST(root):
    return validateBSTHelper(root,float("-inf"),float("inf"))
def validateBSTHelper(root,minValue,maxValue):
    if root is None:
        return True
    elif root.data < minValue or root.data > maxValue:
        return False
    leftIsValid=validateBSTHelper(root.left,minValue,root.data)
    rightIsValid=validateBSTHelper(root.right,root.data,maxValue)
    return leftIsValid and rightIsValid

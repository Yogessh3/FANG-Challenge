class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        root=BST(data)
    else:
        if(data<root.data):
            if root.left is None:
                root.left=BST(data)
            else:
                insert(root.left,data)
        else:
            if root.right is None:
                root.right=BST(data)
            else:
                insert(root.right,data)
    return root
def contains(root,data):
    currentNode=root
    while currentNode is not None and currentNode.data!=data:
        if(data<currentNode.data):
            currentNode=currentNode.left
        else:
            currentNode=currentNode.right
    return 'Found' if currentNode is not None else 'Not Found'
def findMin(root):
    currentNode=root
    while currentNode!=None:
        currentNode=currentNode.left
    return currentNode
def remove(root,data):
    if(data<root.data):
        root.left=remove(root.left,data)
    elif(data>root.data):
        root.right=remove(root.right,data)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=findMin(root.right)
        root.data=temp.data
        root.right=remove(root.right,temp.data)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
N=int(input())
arr=[int(x) for x in input().split()]
root=None
for i in arr:
    root=insert(root,i)
print(root.data)
inorder(root)
print(contains(root,70))
root=remove(root,20)
print(root.data)
inorder(root)



















        

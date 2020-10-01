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
#Time - O(N) / Space - O(N) for all traversals
def inorder(root,array):
    if root is None:
        return None
    inorder(root.left,array)
    array.append(root.data)
    inorder(root.right,array)
    return array
def preorder(root,array):
    if root is None:
        return None
    array.append(root.data)
    preorder(root.left,array)
    preorder(root.right,array)
    return array
def postorder(root,array):
    if root is None:
        return None
    postorder(root.left,array)
    postorder(root.right,array)
    array.append(root.data)
    return array
N=int(input())
arr=[int(x) for x in input().split()]
root=None
for i in arr:
    root=insert(root,i)
print(root.data)
inorderValues=inorder(root,[])
preorderValues=preorder(root,[])
postorderValues=postorder(root,[])
print(*inorderValues)
print(*preorderValues)
print(*postorderValues)

        
    

''' Sample BST

0-->         20
              \
1-->          30
               \
2-->           50
               / \
3-->         40   60
'''
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
#Time - O(N) Space - O(N)
def nodeDepths(root,depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left,depth+1) + nodeDepths(root.right,depth+1)
arr=[20,30,50,60,40]
root=None
for i in arr:
    root=insert(root,i)
print(nodeDepths(root))

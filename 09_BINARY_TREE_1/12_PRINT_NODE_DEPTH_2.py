
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data, end=":")
    if root.left!=None:
        print('L', root.left.data, end=",")
    if root.right!=None:
        print('R', root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData=int(input())
    if rootData == -1:
        return None
    root= BinaryTreeNode(rootData)
    leftTree= treeInput()
    rightTree= treeInput()
    root.left= leftTree
    root.right= rightTree
    return root

def printNodeDepthK2(root,k,d=0):
    if root is None:
        return 0
    if k==d:
        print(root.data, end=' ')
    leftNode= printNodeDepthK2(root.left, k, d+1)
    rightNode= printNodeDepthK2(root.right,k, d+1)




root= treeInput()
printNodeDepthK2(root,2)
# printTreeDetailed(root)


from platform import node


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



def nodeLargestData(root):
    if root is None:
        return -1
    leftTree=nodeLargestData(root.left)
    rightTree= nodeLargestData(root.right)
    largest= max(root.data, leftTree, rightTree)
    return largest



root= treeInput()
print('The largest node is ',nodeLargestData(root))
# printTreeDetailed(root)

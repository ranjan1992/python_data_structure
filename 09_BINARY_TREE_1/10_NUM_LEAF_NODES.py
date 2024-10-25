from turtle import left


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

def numLeafNodes(root):
    if root is None :
        return
    if root.left==None and root.right==None:
        return 1
    leftTree= numLeafNodes(root.left)
    rightTree= numLeafNodes(root.right)
    return leftTree + rightTree


root= treeInput()
print('The number of Leaf Nodes is ',numLeafNodes(root))
printTreeDetailed(root)

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
    leftTree= treeInput() # recursion 
    rightTree= treeInput()  # recursion
    root.left= leftTree
    root.right= rightTree
    return root

root= treeInput()
printTreeDetailed(root)

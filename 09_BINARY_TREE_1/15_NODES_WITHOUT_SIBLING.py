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

def nodeWithoutSib(root):
    if root is None :
        return None
    
    if (root.left !=None and root.right==None) :
        print(root.left.data, end=" ")

    if(root.left==None and root.right!=None):
        print(root.right.data, end=" ")
        
    nodeWithoutSib(root.left)
    nodeWithoutSib(root.right)

root= treeInput()
nodeWithoutSib(root)
# printTreeDetailed(root)

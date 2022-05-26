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


def nodeGreaterX(root,x):
    if root is None:
        return 0
    count=0

    if root.data>x:
        return 1
    if root.left !=None:
        count=count+ nodeGreaterX(root.left,x)
    
    if root.right != None:
        count= count+ nodeGreaterX(root.right,x)
    
    return count


root= treeInput()
print(nodeGreaterX(root, 9))
# printTreeDetailed(root)

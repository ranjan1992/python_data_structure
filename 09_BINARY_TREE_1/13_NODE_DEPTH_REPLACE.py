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

def replaceWithDepth(root):
    replaceWithDepthHelper(root, 0)


def replaceWithDepthHelper(root, d):
    if root is None:
        return None

    root.data=d
    replaceWithDepthHelper(root.left,d+1)
    replaceWithDepthHelper(root.right,d+1)



root= treeInput()
print(replaceWithDepth(root))
printTreeDetailed(root)

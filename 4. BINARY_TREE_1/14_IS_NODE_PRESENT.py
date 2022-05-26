


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

def isNodePresent(root,x):
    if root is None:
        return False
    if root.data==x:
        return True
    leftTree= isNodePresent(root.left, x)
    rightTree= isNodePresent(root.right, x)
    output= leftTree or rightTree
    return output



root= treeInput()
print('The node is', isNodePresent(root,1))
# printTreeDetailed(root)

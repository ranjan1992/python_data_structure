


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

def preOrderTraversal(root):
    if root==None:
        return 
    print( root.data, end=" ")
    leftTree= preOrderTraversal(root.left)
    rightTree= preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root== None:
        return
    leftTree= postOrderTraversal(root.left)
    rightTree= postOrderTraversal(root.right)
    print(root.data, end=" ")

def inOrderTraversal(root):
    if root is None:
        return 
    leftTree= inOrderTraversal(root.left)
    print(root.data, end=" ")
    rightTree= inOrderTraversal(root.right)
    

root= treeInput()
print('Pre-Order Traversal ')
preOrderTraversal(root)
print()
print('Post-Order Traversal ')
postOrderTraversal(root)
print()
print('In-Order Traversal ')
inOrderTraversal(root)
# printTreeDetailed(root)

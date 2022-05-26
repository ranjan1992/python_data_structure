class BinaryTreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class Pair:

    def __init__(self, diameter, height):
        self.diameter=diameter
        self.height=height

def diameterOfBinaryTree(root):
    pair=diameterHelper(root)
    return pair.diameter

def diameterHelper(root):
    if root is None:
        pair= Pair(0,0)
        return pair
    leftPair = diameterHelper(root.left)
    rightPair=diameterHelper(root.right)

    leftDiameter= leftPair.diameter
    rightDiameter = rightPair.diameter

    diameterFromRoot= leftPair.height+ rightPair.height+1

    diameter=max(leftDiameter, rightDiameter, diameterFromRoot)
    height= max(leftPair.height, rightPair.height)+1

    return Pair(diameter, height)



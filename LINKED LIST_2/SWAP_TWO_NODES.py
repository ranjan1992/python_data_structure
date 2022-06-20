class Node :
    def __init__(self, data):
        self.data=data
        self.next=None

def swapNodes(head, i, j):
    if i == j:
        return head

    currentNode = head
    prev = None

    firstNode = None
    secondNode = None
    firstNodePrev = None
    secondNodePrev = None

    pos = 0

    while currentNode is not None:
        if pos == i:
            firstNodePrev = prev
            firstNode = currentNode
        elif pos == j:
            secondNodePrev = prev
            secondNode = currentNode

        prev = currentNode
        currentNode = currentNode.next
        pos += 1

    if firstNodePrev is not None:
        firstNodePrev.next = secondNode
    else:
        head = secondNode

    if secondNodePrev is not None:
        secondNodePrev.next = firstNode
    else:
        head = firstNode

    currentfirstNode = secondNode.next
    secondNode.next = firstNode.next
    firstNode.next = currentfirstNode

    return head


def takeInput():
        inputList= [int(ele) for ele in input().split()]
        head=None
        tail=None

        for currData in inputList:
            if currData ==-1:
                break
            newNode= Node(currData)

            if head is None:
                head =newNode
                tail = newNode
            else:
                tail.next= newNode
                tail = newNode
        return head


def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end=' ')
        head=head.next
    print("None")
head= takeInput()
swapNodes(head, 1, 4)
printLL(head)





     


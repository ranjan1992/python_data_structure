class Node:
    def __init__(self, data):
        self.data =data
        self.next =None


def findNodeRec(head,n):
    if head is None:
        return -1
    
    if head.data == n:
        return 0

    smallAns = findNodeRec(head.next, n)

    if smallAns == -1:
        return -1

    return 1+ smallAns
            


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
n= int(input())
print(findNodeRec(head,n))


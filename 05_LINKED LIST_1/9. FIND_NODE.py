class Node :
    def __init__(self, data):
        self.data= data
        self.next= None

def findNode(head, n):
    curr=head
    count=0
    while curr is not None:
        if curr.data == n:
            return count
        count=count+1
        curr=curr.next
    
    if curr is None:
        return -1
    return count


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

def length(head):
    currData= head
    count=0
    while currData is not None:
        count+=1
        currData=currData.next
    return count


def printLL(head):
    while head is not None:
        print(str(head.data)+" -> ", end=' ')
        head=head.next
    print("None")

head= takeInput()
printLL(head)
data=int(input())

findNode(head,data)
printLL(head)
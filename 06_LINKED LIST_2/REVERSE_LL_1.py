class Node :
    def __init__(self, data):
        self.data=data
        self.next=None

def reverseLinkedListRec(head):
    if head is None or head.next is None:
        return head
    smallHead =reverseLinkedListRec(head.next)
    curr=smallHead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallHead

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

head=reverseLinkedListRec(head)

printLL(head)


     


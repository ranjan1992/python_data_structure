class Node :
    def __init__(self, data):
        self.data= data
        self.next= None

def insertAtI(head, i, data):
    if i<0 or i> length(head):
        return head
    
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count+=1
    newNode= Node(data)
    if prev is not None:
        prev.next= newNode
    else:
        head= newNode
    newNode.next=curr
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

def length(head):
    currData= head
    count=0
    while currData is not None:
        count+=1
        currData=currData.next
    return count


def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end=' ')
        head=head.next
    print("None")
head= takeInput()
printLL(head)
i= int(input())
data=int(input())

insertAtI(head, i, data )
printLL(head)
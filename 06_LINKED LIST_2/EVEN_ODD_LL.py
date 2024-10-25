class Node :
    def __init__(self, data):
        self.data=data
        self.next=None

def evenAfterOdd(head):
    if head is None:
        return head
    evenHead, oddHead, evenTail, oddTail=None,None,None,None

    while head is not None:
        if(head.data%2)==0:
            if evenHead is None:
                evenHead=head
                evenTail=head
            else:
                evenTail.next = head
                evenTail=evenTail.next
        else:
            if oddHead is None:
                oddHead=head
                oddTail = head
            else:
                oddTail.next=head
                oddTail=oddTail.next

        head=head.next

    if oddHead is None:
        return evenHead
    else:
        oddTail.next=evenHead
    
    if evenHead is not None:
        evenTail.next = None
    return oddHead




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

head=evenAfterOdd(head)

printLL(head)



     


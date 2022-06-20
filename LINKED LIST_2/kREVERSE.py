class Node :
    def __init__(self, data):
        self.data=data
        self.next=None

def kReverse(head, k):
    if head is None or head.next is None:
        return head
    h1=head
    tail=head

    count=1
    while tail.next is not None:
        if count ==k:
            break
        count=count+1
        tail=tail.next
    
    h2=tail.next
    tail.next=None
    newh, newt = reverse2(h1)
    newt.next = kReverse(h2, k)

    return newh

def reverse2(head):
    curr=head
    frwd=None
    prev=None
    while curr is not None:
        frwd= curr.next
        curr.next=prev
        prev=curr
        curr=frwd
    return prev, head




   

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
k=int(input())

head=kReverse(head, k)

printLL(head)


     


class Node:
    def __init__(self, data):
        self.data =data
        self.next =None


def mergeTwoSortedLinkedLists(head1, head2):
    if head1==None:
        return head2
    if head2==None:
        return head1
    fH=None
    fT=None 
    
    if head1.data<head2.data:
        fH=head1
        fT=head1
        head1=head1.next
    else:
        fH=head2
        fT=head2
        head2=head2.next
    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
            fT.next=head1
            fT=fT.next
            head1=head1.next
        else:
            fT.next=head2
            fT=fT.next
            head2=head2.next
    while head1 is not None:
        fT.next=head1
        # printLinkedList(fH)
        head1=head1.next
        fT=fT.next
    while head2 is not None:
        fT.next=head2
        head2=head2.next
        fT=fT.next
    return fH
            


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
head1= takeInput()
head2= takeInput()

head=mergeTwoSortedLinkedLists(head1, head2)

printLL(head)
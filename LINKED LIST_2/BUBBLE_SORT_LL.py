class Node :
    def __init__(self, data):
        self.data=data
        self.next=None

def bubbleSortLL(head):
    end=None
    while end != head:
        p=head
        while p.next != end:
            q=p.next
            if p.data > q.data:
                p.data, q.data = q.data, p.data
            p=p.next
        end=p
    return end


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
bubbleSortLL(head)
printLL(head)






     


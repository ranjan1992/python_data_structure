class Node :
    def __init__(self, data):
        self.data= data
        self.next= None

def insertAtIR(head, i, data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next= head
        return newNode
    
    if head is None:
        return None
    
    smallHead = insertAtIR(head.next, i-1, data)
    head.next= smallHead
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
        print(str(head.data)+" -> ", end=' ')
        head=head.next
    print("None")

head= takeInput()
printLL(head)

i= int(input())
data=int(input())

insertAtIR(head,i,data)
printLL(head)
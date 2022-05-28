class Node :
    def __init__(self, data):
        self.data= data
        self.next= None

def printIthNode(head, i):
    currData = head
    count=0
    data1=0

    while currData is not None:
        if count==i:
            data1= currData.data
            print(data1)
            return 
        currData= currData.next
        count+=1
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
printLL(head)
n= int(input())
printIthNode(head, n)

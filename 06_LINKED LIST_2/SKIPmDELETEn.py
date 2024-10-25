class Node :
    def __init__(self, data):
        self.data=data
        self.next=None

def skipMdeleteN(head, M, N) :
    if head is None:
        return head
    if M == 0:
        return None
    temp = head
    prev = None
    cnt = 0
    while temp is not None:
        if(cnt == M):
            break
        cnt += 1
        prev = temp
        temp = temp.next
    cnt = 0
    while temp is not None:
        if(cnt == N):
            break
        cnt += 1
        temp = temp.next
        
    prev.next = skipMdeleteN(temp, M, N)
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


def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end=' ')
        head=head.next
    print("None")
head= takeInput()

M=int(input())
N=int(input())

head1=skipMdeleteN(head, M, N)
printLL(head1)



     


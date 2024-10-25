from shelve import Shelf


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    
class Queue:

    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0

    def getSize(self):
        return self.__count
    
    def isEmpty(self):
        return self.__count==0
    
    def enqueue(self,data):
        newNode=Node(data)
        if self.__head is None:
            self.__head=newNode
            self.__tail=newNode
        else:
            self.__tail.next=newNode
            self.__tail=self.__tail.next
        self.__count=self.__count+1
        return

    def dequeue(self):
        if self.__head is None:
            return -1
        data=self.__head.data
        self.__head=self.__head.next
        self.__count=self.__count-1
        return data
    
    def front(self):
        if self.__head is None:
            return -1
        data= self.__head.data
        return data

q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)

while(q.isEmpty() is False):
    print(q.front())
    q.dequeue()
print(q.dequeue())


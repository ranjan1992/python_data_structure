class Node:

    def __init__(self, data):
        self.data = data
        self.next= None
    
class Stack:
    def __init__(self):
        self.__head = None
        self.__count=0
    
    def getSize(self):
        return self.__count

    def isEmpty(self):
        return self.getSize()==0

    def push(self, data):
        newNode= Node(data)
        newNode.next= self.__head
        self.__head=newNode
        self.__count=self.__count+1
    
    def pop(self):
        if self.isEmpty() is True:
            return -1
        data= self.__head.data
        self.__head = self.__head.next
        self.__count=self.__count-1
        return data
    
    def top(self):
        if self.isEmpty() is True:
            return -1
        data = self.__head.data
        return data

s=Stack()
s.push(12)
s.push(13)
s.push(15)

while s.isEmpty() is False:
    print(s.pop())
s.top()

from sys import stdin

def reverseStack(inputStack, extraStack):
    if len(inputStack)==0:
        return
    lastElement = inputStack.pop()

    reverseStack(inputStack, extraStack)

    while not isEmpty(inputStack):
        top= inputStack.pop()
        extraStack.append(top)
    
    inputStack.append(lastElement)

    while not isEmpty(extraStack):
        top=extraStack.pop()
        inputStack.append(top)

def isEmpty(stack):
    return len(stack)==0

def takeInput():
    size= int(stdin.readline().strip())
    inputStack=list()

    if size==0:
        return inputStack

    values = list(map(int,stdin.readline().strip().split(" ")))
    inputStack = values

    return inputStack

inputStack = takeInput()
emptyStack= list()

reverseStack(inputStack, emptyStack)


while not isEmpty(inputStack) :
    print(inputStack.pop(), end=" ")


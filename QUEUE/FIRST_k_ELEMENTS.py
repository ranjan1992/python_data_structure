
from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    queue1=inputQueue
    queue2=queue.LifoQueue()
    queue3=queue.Queue()
    val=k
    while k>0:
        val=queue1.get()
        queue2.put(val)
        k=k-1
    while not queue2.empty():
        queue3.put(queue2.get())
    while not queue1.empty():
        queue3.put(queue1.get())
    return queue3





























    



'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")

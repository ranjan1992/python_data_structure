from sys import stdin, setrecursionlimit
import queue

def reverseQueue(inputQueue):
    queue1= queue.LifoQueue()
    queue2= inputQueue
    
    while not queue2.empty():
        val=queue2.get()
        queue1.put(val)
    
    while not queue1.empty():
        print(queue1.get(), end=' ')

def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1      

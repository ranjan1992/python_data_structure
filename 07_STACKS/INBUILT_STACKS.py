# inbuilt stack as List
print("Inbuilt Stack as List")
s=[1,2,3,4]
s.append(4)
s.append(5)
print(s.pop())
print(s.pop())

# inbult queue
print("Inbuilt Queue")
import queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
while not q.empty():
    print(q.get())


print("Inbuilt Stack")
import queue
q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())
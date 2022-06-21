import heapq
def kLargest(lst, k):
    n=len(lst)
    li=lst[:k]
    heapq.heapify(li)
    for i in range(k,n):
        if li[0]<lst[i]:
            heapq.heapreplace(li, lst[i])
    return li
        

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')

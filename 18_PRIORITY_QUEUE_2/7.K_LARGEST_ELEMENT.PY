import heapq
def kthLargest(lst, k):
    n=len(lst)
    li=lst[:k]  
    heapq.heapify(li)
    for i in range(k,n):
        if li[0]<lst[i]:
            heapq.heapreplace(li,lst[i])
    return sorted(li)[0]
    


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
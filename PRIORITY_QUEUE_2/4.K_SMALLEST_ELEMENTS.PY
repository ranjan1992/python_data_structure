import heapq
def kSmallest(lst, k):
    n=len(lst)
    li=lst[:k]
    heapq._heapify_max(li)
    for i in range(k,n):
        if li[0]> lst[i]:
            heapq._heapreplace_max(li, lst[i])
    return li   

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')
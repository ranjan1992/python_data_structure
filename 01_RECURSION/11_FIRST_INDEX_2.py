def firstIndex2(a,x,si):
    l=len(a)
    if si==l:
        return -1
    if a[si]==x:
        return si
    smallOp=firstIndex2(a,x,si+1)
    return smallOp

a=[1,23,24,78,9]
print(firstIndex2(a, 23, 0))
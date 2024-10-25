def lastIndex_2(a,x, si):
    l=len(a)
    if si==l:
        return -1
    smallOp=lastIndex_2(a,x,si+1)
    if smallOp !=-1:
        return smallOp
    else:
        if a[si]==x:
            return si
        else: 
            return -1

a=[23,3,1,4,53,23,45,23]

print(lastIndex_2(a, 23, 0))


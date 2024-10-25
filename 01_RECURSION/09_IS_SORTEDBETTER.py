def isSortedBetter(a, si):
    l=len(a)
    if si==l-1 or si==l:
        return True
    if a[si]> a[si+1]:
        return False
    smallOp= isSortedBetter(a, si+1)
    return smallOp
a=[1,23,43,54]
print(isSortedBetter(a,0))

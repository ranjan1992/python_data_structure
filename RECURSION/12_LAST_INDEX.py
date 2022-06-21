def lastIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    smallOp=lastIndex(a[1:],x)
    if smallOp ==-1 and a[0]==x:
        return 0
    elif smallOp !=-1:
        return smallOp+1
    else:
        return -1

a=[1,23,43,23,56,23]
print(lastIndex(a, 23))

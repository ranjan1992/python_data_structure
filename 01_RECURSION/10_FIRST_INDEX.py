def firstIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallOp= firstIndex(a[1:],x)
    if smallOp==-1:
        return -1
    else:
        return smallOp+1

a=[1,23,43,21,54]
x=21
print(firstIndex(a,x))
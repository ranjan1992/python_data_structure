def isSorted(a):
    l= len(a)
    if l==0 or l==1:
        return True
    if a[1]<a[0]:
        return False
    smallOutput= isSorted(a[1:])
    return smallOutput

n=[1,2,4,5,6]
print(isSorted(n))

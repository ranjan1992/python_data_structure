def checkNumber(a,x):
    l=len(a)
    if l==0:
        return False
    if a[0]==x:
        return True
    smallOutput=checkNumber(a[1:],x)
    return smallOutput

n= [1,2,5,34,5]
x=5
print(checkNumber(n,x))


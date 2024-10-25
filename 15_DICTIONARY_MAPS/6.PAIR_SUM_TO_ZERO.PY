from sys import stdin

def pairSum0(l,n):
    d={}
    count=0
    for w in l:
        if w in d:
            d[w]=d[w]+1
        else:
            d[w]=1
    # print(d)
    for w in l:
        if w==0:
            count=count+(d[w]*(d[w]-1))//2
        elif -w in d:
            count=count+d[w]*d[-w]
        d[w]=0
    return count
            








    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))
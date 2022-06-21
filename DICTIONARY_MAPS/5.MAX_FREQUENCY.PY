from sys import stdin
def maxfreq(arr):
    dic={}
    k=arr[0]
    for num in arr:
            dic[num]=dic.get(num,0)+1
    # print(dic)
    for num in arr:
        if dic[num]>dic[k]:
            k=num
    return k
    
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))
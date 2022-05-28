def staircase(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2  
    elif n==3:
        return 4
    return staircase(n-3)+ staircase(n-2) + staircase(n-1) 

n= int(input())
ans= staircase(n)
print(ans)
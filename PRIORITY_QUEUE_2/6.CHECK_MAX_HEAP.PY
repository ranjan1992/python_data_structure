def checkMaxHeap(lst):
    n=len(lst)
    for i in range(n):
        lcI=2*i+1
        rcI=2*i+2
        if lcI<n and lst[i]<lst[lcI]:
            return False
        if rcI<n and lst[i]<lst[rcI]:
            return False
    return True
            
            
    

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
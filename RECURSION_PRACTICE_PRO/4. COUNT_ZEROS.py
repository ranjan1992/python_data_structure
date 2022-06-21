def countZeroes(n):
    if n<10:
        if n==0:
            return 1
        return 0
    smallAns = countZeroes(n//10)
    if n%10==0:
        smallAns +=1
    return smallAns


from sys import setrecursionlimit
setrecursionlimit(11000)
n= int(input())
print(countZeroes(n))

def fact(n):
    if n==0:
        return 1
    smaddllOp=fact(n-1)
    return n*smaddllOp

n=int(input())
print(fact(n))


def factHelper(n):
    if n==0:
        return 1
    smallOutput=factHelper(n-1)
    output=n*smallOutput
    return output

def fact(n):
    output=factHelper(n)
    print(output)


fact(5)


def printFact(n,ans):
    if n==0:
        print(ans)
        return
    ans=ans*n
    printFact(n-1,ans)


printFact(5,1)
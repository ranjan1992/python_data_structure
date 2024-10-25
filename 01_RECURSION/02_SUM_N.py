def sum_n(n):
    if n==0:
        return 0
    smallOp= sum_n(n-1)
    output=smallOp+n
    return output

n=int(input())
print(sum_n(n))
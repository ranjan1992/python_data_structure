def power_n(x,n):
    if n==0:
        return 1
    if n%2==0:
        smallOp= power_n(x*x,n//2)
    else:
        smallOp= x*power_n(x*x, n//2)
    return smallOp
x= int(input("Enter the number x = "))
n= int(input("Enter the number n = "))

print(power_n(x,n))

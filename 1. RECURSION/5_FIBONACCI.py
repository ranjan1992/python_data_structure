def fib(n):
    if n==1 or n==2:
        return 1
    fib_1=fib(n-1)
    fib_2=fib(n-2)
    output=fib_1+fib_2
    return output

n=int(input("The fibonacci number : "))

print(fib(n))
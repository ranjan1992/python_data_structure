def geometricSum(num):
    n=num
    if n==0:
        return 1
    i=(1/2)**n
    sum=i+geometricSum(num-1)
    return sum

num= int(input("Enter the number :"))

val=geometricSum(num)
print('%0.5f' % val)
def sumOfDigits(number):
    if number==0:
        return 0
    sum= number%10
    num=number//10
    output=sum+sumOfDigits(num)
    return output

s=int(input())
print(sumOfDigits(s))
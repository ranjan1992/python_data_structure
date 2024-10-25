from sys import stdin

def stockSpan(price, n):
    s=[]
    spans=[]
    s.append(0)
    spans.append(1)
    for i in range(1, len(price)):
        if price[i]<=price[s[-1]]:
            spans.append(1)
            s.append(i)
        else:
            while len(s)>0 and price[i]> price[s[-1]]:
                s.pop()
            if len(s)==0:
                spans.append(i+1)
            else:
                spans.append(i-s[-1])
            s.append(i)
    return spans

n= int(input())
price = [60,70,80,100,90,75,80,120]
print(stockSpan(price,n))

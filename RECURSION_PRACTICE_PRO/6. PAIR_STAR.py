def identicalChar(string):
    l=len(string)
    if(l==1):
        return string
    output1= identicalChar(string[1:])
    if(string[0]==string[1]):
        output1= string[0]+'*'+string[1]
        return output1
    else: 
        output1= string[0]+output1
        return output1

s=input()
print(identicalChar(s))
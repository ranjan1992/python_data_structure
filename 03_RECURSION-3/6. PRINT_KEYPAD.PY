def getString(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return ""

def printkeypad(n,outputSoFar):
    if n==0:
        print(outputSoFar)
        return
    smallNumber=n//10
    lastDigit=n%10
    
    optionsForLastDigit=getString(lastDigit)
    for c in optionsForLastDigit:
        newOutput=c+outputSoFar
        printkeypad(smallNumber,newOutput)

printkeypad(23,"")
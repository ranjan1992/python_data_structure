# pippi= 3.14p3.14

def replacePi(s):
    l=len(s)
    if l==0 or l==1:
        return s
    if s[0]=='p' and s[1]=='i':
        smallOp= replacePi(s[2:])
        return '3.14'+smallOp
    else:
        smallOp=replacePi(s[1:])
        return s[0]+smallOp

print(replacePi("ppipppi"))


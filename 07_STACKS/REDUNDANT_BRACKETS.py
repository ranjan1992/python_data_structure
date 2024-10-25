def checkRedundantBrackets(str):
    s=[]
    for char in str:
        if char == '(':
            s.append(char)
        elif char in '+-/*':
            s.append(char)
        elif char == ')':
            if len(s)!=0 and s[-1] in '+-/*':
                while s[-1]!='(':
                    s.pop()
                s.pop()
            else:
                return True
    return False

str= input()
print(checkRedundantBrackets(str))

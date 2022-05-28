def StringTOInteger(string):
    l=len(string)
    if(l==1):
        return int(string)
    output= StringTOInteger(string[:l-1])
    return output*10 + int(string[-1])

s= input()
print(type(s))
print(StringTOInteger(s))
print(type(StringTOInteger(s)))

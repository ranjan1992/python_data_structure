def removeX(str):
    if len(str)==0:
        return str
    if str[0]=='x':
        return removeX(str[1:])
    return str[0]+ removeX(str[1:])

string = input()
print(removeX(string))



from os import remove


def removeDR(str):
    l=len(str)
    if l==1:
        return str
    if str[0]==str[1]:
        return removeDR(str[1:])
    else:
        return str[0]+removeDR(str[1:])

string= input()
print(removeDR(string))
def uniqueChar(s): 
    dict={}
    s_new=""
    for char in s:
        if char in dict:
            s_new=s_new+""
        else:
            s_new=s_new+char
            dict[char]=1
    return s_new
            





# Main 
s=input() 
print(uniqueChar(s))
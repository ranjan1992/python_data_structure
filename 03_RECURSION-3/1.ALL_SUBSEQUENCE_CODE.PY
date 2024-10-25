def subs(s):
    if len(s)==0:
        output=[]
        output.append("")
        return output
    smallerString=s[1:]
    smallerOutput=subs(smallerString)
    
    output=[]
    for sub in smallerOutput:
        output.append(sub)
        
    for sub in smallerOutput:
        subs_with_zeroth_char=s[0]+sub
        output.append(subs_with_zeroth_char)
        
    return output

subs("abcd")
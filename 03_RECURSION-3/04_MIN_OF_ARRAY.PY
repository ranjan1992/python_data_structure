def minList(l):
    if len(l)==1:
        return l[0]
    
    minSmallArray=minList(l[1:])
    overallMin=min(minSmallArray,l[0])
    return overallMin

def printMin(l,minSoFar=100000):
    if len(l)==0:
        print(minSoFar)
        return
    newMin=min(minSoFar,l[0])
    printMin(l[1:],newMin)

printMin([1,2,3,4,-1,0,-2,-4,5,6])
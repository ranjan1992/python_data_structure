def binarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return binarySearch(a,x,si,mid-1)
    else:
        return binarySearch(a,x,mid+1,ei)

print(binarySearch([1,3,5,7,9,11,13,15,16,17],11,0,9))

print(binarySearch([1,3,5,7,9,11,13,15,16,17],2,0,9))

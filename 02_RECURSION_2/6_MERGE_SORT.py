def merge(a1,a2,a):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            i=i+1
            k=k+1
        else:
            a[k]=a2[j]
            j=j+1
            k=k+1
    
    while i<len(a1):
        a[k]=a1[i]
        i=i+1
        k=k+1
    
    while j<len(a2):
        a[k]=a2[j]
        j=j+1
        k=k+1

def mergeSort(a):
    l=len(a)
    if l==0 or l==1:
        return
    mid=len(a)//2
    a1=a[0:mid]
    a2=a[mid:]

    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,a)

array=[10,5,3,1,7,9,4]

mergeSort(array)


print(array)
    
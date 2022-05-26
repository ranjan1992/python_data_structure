def sum_array(a):
    l=len(a)
    if l==0:
        return 0
    smallOutput= sum_array(a[1:])
    output= smallOutput+a[0]
    return output
n=[1,2,78,23]
print(sum_array(n))
    
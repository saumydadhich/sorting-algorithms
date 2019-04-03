
def mergeSort(array):
    if len(array)==1:
        return array
    mid = len(array)//2
    left= mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left,right)

def merge(left, right):
    i=0
    j=0
    k=0
    S =[]
    l1=len(left)
    l2=len(right)
    while(i<l1 and j<l2):
        if left[i] <= right[j]:
            S.append(left[i])
            i=i+1
        elif left[i] > right[j]:
            S.append(right[j])
            j=j+1
        k=k+1
    
    while(i<l1):
        S.append(left[i])
        i=i+1
        k=k+1
    while(j<l2):
        S.append(right[j])
        j=j+1
        k=k+1            
    return S
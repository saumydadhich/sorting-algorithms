def quickSort(arr,x, y):
    def swapElements(arr,x, y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
    if x >= y: 
        return
    pivot = arr[y]              #Choose pivot as last element of array arr
    left = x
    right = y - 1
    while left <= right:
        while left <= right and arr[left] <= pivot: 
            left += 1   
        while left <= right and arr[right] > pivot: 
            right -= 1  
        if left < right: 
            swapElements(arr, left, right)
    swapElements(arr, left, y)
    quickSort(arr, x, left-1) 
    quickSort(arr, left+1, y)
    return arr
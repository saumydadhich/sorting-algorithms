
def insertionSort(sort_list, min, max):
    for i in range(min, max + 1):
        key = sort_list[i]
        j = i - 1
        while j >= min and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    return sort_list
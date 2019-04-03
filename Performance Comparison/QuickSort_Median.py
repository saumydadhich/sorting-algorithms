from InsertionSort import insertionSort

def calcMedian(array, min, max):
    mid = int((max + min) / 2)
    if array[min] > array[mid]:
        array[min], array[mid] = array[mid], array[min]
    if array[min] > array[max]:
        array[max], array[min] = array[min], array[max]
    if array[mid] > array[max]:
        array[max], array[mid] = array[mid], array[max]
    return mid


def quicksort_median(array, min, max):
    if max - min >= 10:
        pivot_index = calcMedian(array, min, max)
        array[pivot_index], array[max - 1] = array[max - 1], array[pivot_index]
        pivot_index = max - 1
        l_index = min
        r_index = max - 2
        bool = True
        while bool:
            while array[l_index] <= array[pivot_index] and l_index <= r_index:
                l_index += 1
            while array[r_index] > array[pivot_index] and r_index >= l_index:
                r_index -= 1
            if l_index < r_index:
                array[l_index], array[r_index] = array[r_index], array[l_index]
            else:
                bool = False
        array[l_index], array[pivot_index] = array[pivot_index], array[l_index]
        pivot_index = l_index
        quicksort_median(array, min, l_index - 1)
        quicksort_median(array, l_index + 1, max)
    else:
        array = insertionSort(array, min, max)
    return array

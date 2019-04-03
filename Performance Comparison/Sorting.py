import copy
import random
from sys import setrecursionlimit
import time

from InsertionSort import insertionSort
from MergeSort import mergeSort
from QuickSort import quickSort
from QuickSort_Median import quicksort_median

setrecursionlimit(100000)

n = int(input("Enter the number of elements to be sorted: "))

#Generate random numbers for the given number of elements 
content =[]
for x in range(n):
    content.append(random.randint(1,int(0.95*n)))
#Perform insertion sort and take average time by running it thrice
avgTimeArray=[]
for x in range(3):
    input1=copy.deepcopy(content)
    start=time.time();
    result = insertionSort(input1, 0, len(content)-1)
    end=time.time()
    timeElapsed= end - start
    avgTimeArray.append(timeElapsed)
temp=0.0
for x in range(3):
    temp+=avgTimeArray[x]
avgTime=temp/3
print("Execution time for Insertion Sort is:",avgTime)

#Perform merge sort and take average time by running it thrice
avgTimeArray=[]
for x in range(3):
    input2=copy.deepcopy(content)
    start=time.time();
    result = mergeSort(input2)
    end=time.time()
    timeElapsed= end - start
    avgTimeArray.append(timeElapsed)
temp=0.0
for x in range(3):
    temp+=avgTimeArray[x]
avgTime=temp/3
print("Execution time for Merge Sort is:",avgTime)

#Perform in-place quick sort and take average time by running it thrice
avgTimeArray=[]
for x in range(3):
    input3=copy.deepcopy(content)
    start=time.time();
    result = quickSort(input3,0,len(input3)-1)
    end=time.time()
    timeElapsed= end - start
    avgTimeArray.append(timeElapsed)
temp=0.0
for x in range(3):
    temp+=avgTimeArray[x]
avgTime=temp/3
print("Execution time for Quick Sort is:",avgTime)

#Perform modified quick sort and take average time by running it thrice
avgTimeArray=[]
for x in range(3):
    input4=copy.deepcopy(content)
    start=time.time();
    result = quicksort_median(input4,0,len(input4)-1)
    end=time.time()
    timeElapsed= end - start
    avgTimeArray.append(timeElapsed)
temp=0.0
for x in range(3):
    temp+=avgTimeArray[x]
avgTime=temp/3
print("Execution time for Quick Sort using median of 3 is:",avgTime)

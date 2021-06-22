#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:24:56 2021

@author: evelynebushuru
"""

def quicksortalgo(array):
    newArray = array[:]
    pointerIdx =0
    leftPointer = 1
    rightPointer =len(newArray)-1
    quicksortHelper(newArray,pointerIdx,leftPointer,rightPointer)
    return newArray
    
def swap(firstIdx,secondIdx, newArray):
    newArray[firstIdx],newArray[secondIdx] = newArray[secondIdx],newArray[firstIdx]


def quicksortHelper(newArray,pointerIdx,leftPointer,rightPointer):
    if leftPointer>=rightPointer:# and newArray[pointerIdx]<=newArray[rightPointer]:
        return
    while rightPointer >= leftPointer:
        if newArray[leftPointer]>newArray[pointerIdx] and newArray[rightPointer]< newArray[pointerIdx]:
            swap(leftPointer,rightPointer,newArray)
            leftPointer += 1
            rightPointer -= 1
        elif newArray[leftPointer] <= newArray[pointerIdx]:
            leftPointer += 1
        elif newArray[rightPointer]>= newArray[pointerIdx]:
            rightPointer -= 1
        print(leftPointer,rightPointer,newArray)
    swap(pointerIdx,rightPointer,newArray)
    print(newArray)

    leftisSmaller = rightPointer-pointerIdx<(len(newArray)-1)-rightPointer
    print(leftisSmaller)
    if leftisSmaller:
        quicksortHelper(newArray,pointerIdx,pointerIdx+1,rightPointer-1)
        quicksortHelper(newArray,rightPointer+1,rightPointer+2,len(newArray)-1)
    else:
        quicksortHelper(newArray,rightPointer+1,rightPointer+2,len(newArray)-1)
        quicksortHelper(newArray,pointerIdx,pointerIdx+1,rightPointer-1)
    print(newArray)

print(quicksortalgo([4,53,2,6,-2,5]))

# def quicksortalgo(array):
#     #array=somearray[:]
#     quicksortHelper(array,0,len(array)-1)
#     return array
# def quicksortHelper(array,startIdx,endIdx):
#     pivotIdx = startIdx
#     leftPointer = startIdx+1
#     rightPointer = endIdx
#     if startIdx >= rightPointer:
#         return
#     while leftPointer<= rightPointer:
#         if array[leftPointer]> array[pivotIdx] and array[rightPointer]< array[pivotIdx]:
#             swap(leftPointer,rightPointer,array)
#             leftPointer+=1
#             rightPointer-=1
#         elif array[leftPointer]<= array[pivotIdx]:
#             leftPointer += 1
#         elif array[rightPointer]>= array[pivotIdx]:
#             rightPointer -= 1
#         print([array,leftPointer,rightPointer])
#     swap(pivotIdx,rightPointer,array)
#     print([array,leftPointer,rightPointer])
#     leftisSmaller= rightPointer-1-startIdx< endIdx-(rightPointer+1)
#     if leftisSmaller:
#         quicksortHelper(array,startIdx,rightPointer-1)
#         quicksortHelper(array,rightPointer+1,endIdx)
#     else:
#         quicksortHelper(array,rightPointer+1,endIdx)
#         quicksortHelper(array,startIdx,rightPointer-1)

# def swap(first,second,array):
#     array[first],array[second]= array[second],array[first]
    
# print(quicksortalgo([4,53,2,6,-2,5,5,5]))

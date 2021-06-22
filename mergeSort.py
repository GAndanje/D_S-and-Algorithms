#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:59:32 2021

@author: evelynebushuru
"""

def mergeSort(array):
    if len(array) <=1: 
        return array
    middleIdx = len(array)//2
    leftArray = array[:middleIdx]
    rightArray = array[middleIdx:]
    print(leftArray,rightArray)
    return domerge(mergeSort(leftArray),mergeSort(rightArray))



def domerge(left,right):
    sortedArray=[0]*(len(left)+len(right))
    print(sortedArray)
    leftPointer=rightPointer=sortedarrayPointer= 0
    while leftPointer  < len(left) and rightPointer <len(right):
        if left[leftPointer]<=right[rightPointer]:
            sortedArray[sortedarrayPointer]=left[leftPointer]
            leftPointer+=1
        else:
            sortedArray[sortedarrayPointer]=right[rightPointer]
            rightPointer+=1
        sortedarrayPointer += 1
    print(sortedArray)
    while leftPointer< len(left):
        sortedArray[sortedarrayPointer]= left[leftPointer]
        leftPointer+=1
        sortedarrayPointer+=1
    while rightPointer<len(right):
        sortedArray[sortedarrayPointer]= right[rightPointer]
        rightPointer += 1
        sortedarrayPointer += 1
    print(sortedArray)
    return sortedArray

print(mergeSort([4,53,2,6,-2]))

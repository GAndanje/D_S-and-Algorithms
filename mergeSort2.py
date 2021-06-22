#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:21:21 2021

@author: evelynebushuru
"""

def mergeSort(mainArray):
    if len(mainArray) <=1:
        return mainArray
    auxilliaryArray = mainArray[:]
    mergeSorthelper(mainArray,auxilliaryArray,0,len(mainArray)-1)
    return mainArray

def mergeSorthelper(mainArray,auxilliaryArray,startIdx,endIdx):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx+endIdx)//2
    print(middleIdx)
    mergeSorthelper(auxilliaryArray, mainArray, startIdx, middleIdx)
    print(auxilliaryArray,startIdx,endIdx)
    mergeSorthelper(auxilliaryArray, mainArray, middleIdx+1, endIdx)
    print(auxilliaryArray,middleIdx,endIdx)
    domerge(mainArray, auxilliaryArray, startIdx, endIdx,middleIdx)

def domerge(mainArray,auxilliaryArray,startIdx,endIdx,middleIdx):
    mainArraypointer=startIdx
    auxilliaryleftpointer = startIdx
    auxilliaryrightpointer = middleIdx+1
    while auxilliaryleftpointer<=middleIdx and auxilliaryrightpointer<=endIdx:
        if auxilliaryArray[auxilliaryleftpointer]<=auxilliaryArray[auxilliaryrightpointer]:
            mainArray[mainArraypointer]=auxilliaryArray[auxilliaryleftpointer]
            auxilliaryleftpointer += 1
        else:
            mainArray[mainArraypointer]=auxilliaryArray[auxilliaryrightpointer]
            auxilliaryrightpointer += 1
        mainArraypointer += 1
    print(mainArray,auxilliaryArray)
    while auxilliaryleftpointer <= middleIdx:
        mainArray[mainArraypointer] = auxilliaryArray[auxilliaryleftpointer]
        auxilliaryleftpointer += 1
        mainArraypointer += 1
    print(mainArray,auxilliaryArray)
    while auxilliaryrightpointer <= endIdx:
        mainArray[mainArraypointer] = auxilliaryArray[auxilliaryrightpointer]
        auxilliaryrightpointer += 1
        mainArraypointer += 1
    print(mainArray,auxilliaryArray)
    return mainArray

print(mergeSort([4,53,2,6,-2]))

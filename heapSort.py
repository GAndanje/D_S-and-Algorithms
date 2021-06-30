#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:57:03 2021

@author: evelynebushuru
"""
def heapSort(array):
    childIdx = len(array)-1
    return sortArray(maxHeap(array,len(array)//2-1,childIdx))

def maxHeap(array,lastIdx,childIdx):
    parentIdx = lastIdx
    if isRightChild(childIdx):
        parentIdx=(childIdx-2)//2
    else:
        parentIdx=(childIdx-1)//2
    if parentIdx>=0:
        print(parentIdx)
        if array[childIdx]>array[parentIdx]:
            swap(array,childIdx,parentIdx)
            maxHeap(array,childIdx,parentIdx)
            print(array)
        else:
            childIdx -=1
        maxHeap(array,parentIdx,childIdx)
    return array

def swap(array,childIdx,parentIdx):
    array[childIdx],array[parentIdx]= array[parentIdx],array[childIdx]
    
def isRightChild(childIdx):
    return (childIdx-2)%2==0

def sortArray(array):
    idxtoswap = len(array)-1
    while idxtoswap >0:
        print(f'heapified: {array}')
        swap(array,idxtoswap,0)
        print(f'swapped: {array}')
        maxHeapify(array,0,idxtoswap)
        idxtoswap -=1
    return array
def maxHeapify(array,bubbleDownIdx,idxtoswap):
    parentIdx=bubbleDownIdx
    leftChild = rightChild = False
    left= parentIdx*2+1
    if left < idxtoswap:
        leftChild= left
    right = parentIdx*2+2
    if right < idxtoswap:
        rightChild = right
    if leftChild and rightChild:
        if array[leftChild]> array[rightChild]:
            childIdx2swap = leftChild
            
        else:
            childIdx2swap = rightChild
    elif leftChild is None:
        if array[rightChild]>array[parentIdx]:
            childIdx2swap= rightChild
    elif rightChild is None:
        if array[leftChild]>array[parentIdx]:
            childIdx2swap = leftChild
    else:
        childIdx2swap = idxtoswap
    if childIdx2swap < idxtoswap:
        if array[childIdx2swap]>array[parentIdx]:
            swap(array,childIdx2swap,parentIdx)
            maxHeapify(array,childIdx2swap,idxtoswap)
print(heapSort([39, 4, 53, 3,-1,0,20,24,12,7,2,15,11]))

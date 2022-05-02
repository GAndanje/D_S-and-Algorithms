#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:57:03 2021

@author: evelynebushuru
"""
def heapSort(array):
    parentIdx=len(array)//2-1
    for i in reversed(range(parentIdx+1)):
        maxHeap(array,i)
    return sortArray(array)

def maxHeap(array,parentIdx):
    print('NOW CREATING HEAP')
    largest = parentIdx*2+1 if parentIdx*2+1<len(array) and array[parentIdx*2+1]>array[parentIdx] else parentIdx
    # if parentIdx*2+2 < len(array) and array[parentIdx*2+2]>array[largest]:
    #     largest =parentIdx*2+2
    largest = parentIdx*2+2 if parentIdx*2+2<len(array) and array[parentIdx*2+2]>array[largest] else largest
    if largest != parentIdx:
        swap(array,largest,parentIdx)
        maxHeap(array,largest)
        print(array)
    return array

def swap(array,childIdx,parentIdx):
    array[childIdx],array[parentIdx]= array[parentIdx],array[childIdx]


def sortArray(array):
    print('NOW SORTING HEAP')
    for index in reversed(range(1,len(array))):
        swap(array,index,0)
        print(f'swapnext{array}')
        maxHeapify(array,(index+1)//2-1,index)
        print(f'maxhaeping: {array}')
    return array
def maxHeapify(array,parentIdx,lastIdx):
    for i in reversed(range(parentIdx+1)):
        largestIdx=i*2+1 if i*2+1<lastIdx and array[i*2+1] >array[i] else i
        largestIdx=i*2+2 if i*2+2<lastIdx and array[i*2+2] >array[i] else largestIdx
        if largestIdx !=i:
            swap(array,largestIdx,i)
            # print(f'minswaping: {array}')
            maxHeapify(array,largestIdx,lastIdx)
            # print(f'minmaxing: {array}')

print(heapSort([39, 4, 53,6, 9,1,6,-34,774,0]))
                        #     39                   0            9
                        #    /   \                /  \         / \
                        #   4     53             1    28      4    1
                        #  /  \   /             / \   /      /
                        # 6    9  1            3   4  53    6

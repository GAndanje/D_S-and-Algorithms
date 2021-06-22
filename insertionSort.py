#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:12:13 2021

@author: evelynebushuru
# """

# def insertionsortAlgo(array):#not much insertion sort rather is my own trial and is more of selection sort
#     sortedPointer,unsortedPointer = 0,1
#     for num in array:
#         while unsortedPointer < len(array):
#             if array[unsortedPointer]< array[sortedPointer]:
#                 array[unsortedPointer],array[sortedPointer]=array[sortedPointer],array[unsortedPointer]
#                 unsortedPointer += 1
#             else:
#                 unsortedPointer += 1
#         sortedPointer += 1
#         unsortedPointer =sortedPointer+1
#         print(unsortedPointer,len(array))
#     return array
# print(insertionsortAlgo([2, 4, 53, 6, -2]))

def insertionsortAlgo(array):
    for i in range(1,len(array)):
        j=i
        while j>0 and array[j]<array[j-1]:
            swap(j,j-1,array)
            j -= 1
    return array

def swap(left,right,someArray):
    someArray[left],someArray[right]=someArray[right],someArray[left]



print(insertionsortAlgo([4,53,2,6,-2]))

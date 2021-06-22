#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:30:02 2021

@author: evelynebushuru
"""
import insertionSort
def threenoSum(array,target):
    listofthrees = []
    assignedArray = insertionSort.insertionsortAlgo(array)
    pointer,rightpointer= 0,len(assignedArray)-1
    leftpointer=pointer+1
    while pointer < len(assignedArray)-2:
        while rightpointer>leftpointer:
            if sum([assignedArray[rightpointer],assignedArray[leftpointer],assignedArray[pointer]])>target:
                rightpointer -= 1
            elif sum([assignedArray[rightpointer],assignedArray[leftpointer],assignedArray[pointer]])<target:
                leftpointer += 1
            elif sum([assignedArray[rightpointer],assignedArray[leftpointer],assignedArray[pointer]])==target:
                 listofthrees.append([assignedArray[pointer],assignedArray[leftpointer],assignedArray[rightpointer]])
                 leftpointer+=1
                 rightpointer-=1
        pointer+=1
        leftpointer,rightpointer = pointer+1,len(assignedArray)-1
    return listofthrees

print(threenoSum([4,53,2,6,-2],4))

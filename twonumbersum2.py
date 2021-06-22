#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:10:35 2021

@author: evelynebushuru
"""


def twonumberSum(unsorttedarray,targetSum):
    array=sortArray(unsorttedarray)
    leftPointer,rightPointer = 0,len(array)-1
    while leftPointer<rightPointer:
        if array[leftPointer]+array[rightPointer]==targetSum:
            return [array[leftPointer],array[rightPointer]]
        elif array[leftPointer]+array[rightPointer]>targetSum:
            rightPointer -= 1
        else:
            leftPointer += 1
            
    return
def sortArray(unsorttedarray):
    
    
    return unsorttedarray


print(twonumberSum([7,8,2,5,12,1], 10))

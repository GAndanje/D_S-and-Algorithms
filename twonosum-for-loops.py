#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:56:02 2021

@author: evelynebushuru
"""

def twonumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstnum = array[i]
        for j in range(i+1,len(array)):
            secondnum = array[j]
            if firstnum+secondnum == targetSum:
                return [firstnum,secondnum]
    return[]
print(twonumberSum([7,8,9,5,12,1], 10))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:56:14 2021

@author: evelynebushuru
"""

def twonumberSum(array,targetSum):
    dictionary = {}
    for num in array:
        if targetSum-num in dictionary:
            return [targetSum-num,dictionary[targetSum-num],dictionary]
        else:
            dictionary[num]=targetSum-num
    return
    
print(twonumberSum([7,8,9,5,12,1], 10))

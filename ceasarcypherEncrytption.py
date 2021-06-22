#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 23:00:04 2021

@author: evelynebushuru
"""

def ceasarcypherAlgo(string,key):
    encrypted =[i for i in string]
    if key > 25:
        key = key%25
    for i in range(len(encrypted)):
        if ord(encrypted[i])+key > 122:
            encrypted[i]=chr((96+ord(encrypted[i])+key)%122)
        else:
            encrypted[i]= chr(ord(encrypted[i])+key)
    return encrypted

print(ceasarcypherAlgo('stringz',2))

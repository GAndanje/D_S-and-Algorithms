#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 12:17:55 2021

@author: evelynebushuru
"""

def topolicalsortAlgo(items,capacity):
    myKnapsackvalues =[[0 for x in range(capacity+1)]for y in range(len(items))]
    for rows in range(1,len(items)):
        for columns in range(capacity+1):
            if items[rows][1]> columns:
                myKnapsackvalues[rows][columns] = myKnapsackvalues[rows-1][columns]
            else:
                myKnapsackvalues[rows][columns] =maximum(rows,columns,items,myKnapsackvalues)
        print(myKnapsackvalues)
    # highvalueitems =[]
    # done = False
    # maximumcolumn,maximumrow =capacity+1,len(items)+1
    # print(myKnapsackvalues)
    # while not done:
    #     if maximumrow == maximumcolumn == 0:#myKnapsackvalues[maximumrow][maximumcolumn]==0:
    #         done=True
    #     if myKnapsackvalues[maximumrow][maximumcolumn] == myKnapsackvalues[maximumrow-1][maximumcolumn]:
    #         maximumrow -=1
    #     else:
    #         highvalueitems.append(items[maximumrow])
    #         maximumcolumn -= items[maximumrow][1]
    #         maximumrow -=1
    return myKnapsackvalues

def maximum(rows,columns,items,myKnapsackvalues):
    maximumvalue = max(myKnapsackvalues[rows-1][columns],myKnapsackvalues[rows-1][columns-items[rows][1]]+items[rows][0]) #[rows-1-(items[rows][1])+items[rows][0]])
    return maximumvalue

print(topolicalsortAlgo([[4,3],[1,2],[5,1],[3,7],[6,5]],10))
# capacity=10
# items=[[4,3],[1,2],[5,1],[3,7],[6,5]]
# myKnapsackvalues =[[0 for x in range(capacity+1)]for y in range(len(items)+1)]
# print(myKnapsackvalues)

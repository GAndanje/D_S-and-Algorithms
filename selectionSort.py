# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon May 31 16:44:35 2021

# @author: evelynebushuru
# """

# def selectionSort(array):
#     for num in range(len(array)-1):
#         smallestIdx = num
#         pointer = num
#         while pointer < len(array)-1:
#             if array[pointer+1]< array[smallestIdx]:
#                 smallestIdx =pointer+1
#                 pointer += 1
#             else:
#                 pointer += 1
#         swap(num,smallestIdx,array)
            
#     return array

# def swap(formersmallIdx,currentsmallIdx,array):
#     array[formersmallIdx],array[currentsmallIdx] = array[currentsmallIdx],array[formersmallIdx]
    
# print(selectionSort([3,4,1,-1.,5,-3,22,4-3]))

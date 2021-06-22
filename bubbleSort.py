
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun May 30 12:12:13 2021

# @author: evelynebushuru
# """

# def bubblesortAlgo(array):
#     value = False
#     for pointer in range(len(array)-1):
#         if array[pointer+1]<array[pointer]:
#             swap(pointer,pointer+1,array)
#             pointer += 1
#             value=True
#         else:
#             pointer += 1
#     if value:
#         bubblesortAlgo(array)
            
#     return array

# def swap(first,second,array):
#     array[first],array[second] = array[second],array[first]

# print(bubblesortAlgo([4,53,2,6,-2]))

def bubblesortAlgo(array):
    isSorted= False
    rangecount = len(array)-1
    while not isSorted:
        isSorted= True
        for num in range(rangecount):
            if array[num] > array[num+1]:
                swap(num,num+1,array)
                isSorted= False
        rangecount -= 1
    return array
def swap(num,num1,array):
    array[num],array[num1] = array[num1],array[num]

print(bubblesortAlgo([3,4,1,-1.,5,-3,22,4-3]))

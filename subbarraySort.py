# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun  2 17:39:03 2021

# @author: evelynebushuru
# """

# def unsortedSubarray(array):
#     unsortednumList= []
#     sortedDict = {}
#     sortedList= []
#     pointer =0
#     while pointer < len(array)-1:
#         if array[pointer+1]<array[pointer]:
#             unsortednumList.append(array[pointer])
#             print(unsortednumList)
#             pointer += 1
#         else:
#             sortedDict[array[pointer]] = pointer
#             pointer += 1
#     maxunsorted = max(unsortednumList)
#     minunsorted = min(unsortednumList)
#     sortedList = sortedDict.keys()
#     minmaxpointer = 0
#     while sortedList[minmaxpointer]<= minunsorted:
#         minindex =sortedList[minmaxpointer]
#         minmaxpointer += 1
#     minmaxpointer = len(sortedList)-1
#     while sortedList[minmaxpointer]>= maxunsorted:
#         maxindex = sortedList[minmaxpointer]
#         minmaxpointer -= 1
#     return (minindex,maxindex)

# print(unsortedSubarray([1,3,4,5,-2,4,5,5,0,9,3,6,8,9,20]))

def sortSubarray(array):
    minUnsorted,maxUnsorted,index= float('inf'), float('-inf'),0
    while index < len(array)-1:
        if array[index+1]< array[index]:
            minUnsorted= min(minUnsorted,array[index+1])
            maxUnsorted= max(maxUnsorted,array[index])
            print(f"we are in the while loop1 if branch {minUnsorted,maxUnsorted}")
            index += 1
            
        else:
            print(f"we are in the while loop 1 else branch {minUnsorted,maxUnsorted}")
            index += 1
    print(f"we are out of the while loop1{minUnsorted,maxUnsorted}")
    index = 0
    finished = False
    minIdx=maxIdx =0
    while not finished:
        if array[1] < array[0]:
            minIdx = 0
        if array[-1] < array[-2]:
            maxIdx= len(array)-1
        while index < len(array)-1: #and array[index+1] >= array[index]:
            if array[index+1] > minUnsorted:
                minIdx = index+1
                index = len(array)-1
            else:
                index +=1
        index =len(array)-1
        while index>0:
            if array[index-1]< maxUnsorted:
                maxIdx=index-1
                index=0
            else:
                index -=1
        finished = True
    return [minIdx,maxIdx,array[minIdx:maxIdx+1],len(array),len(array[minIdx:maxIdx+1])]
print(sortSubarray([1,2,4,5,9,3,6,5,10,20,30]))

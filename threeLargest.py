# import numpy
# listTosort = list(numpy.random.randint(1,20,20))
# print(listTosort)
# listSorted = list.sort(listTosort)
# print(listTosort)

# def threeLargenums(listUnsorted):
#     largest = listUnsorted[-1]
#     i = -2
#     while listUnsorted[i] != largest:
#         secondLargest = listUnsorted[i]

#     return [largest, secondLargest, thirdLargest]
# threeLargenums(listTosort)

# def threeLargestnumbers(myArray):
#     theLargestlist = [None, None, None]
#     for i in len(myArray):
#         for j in len(theLargestlist):
#             if theLargestlist[j-1] == none || theLargestlist[j-1] < myArray[i-1]:
#                 updateLargestarray(theLargestlist,index,number)
#             elif theLargestlist[j-1] > myArray[i-1]:
#                 j += 1
#             else:
#                 return theLargestlist

# def updateLargestarray(theLargestlist,index,number)
import numpy

dataArray = list(numpy.random.randint(1,50,50))
print(dataArray)
largestThreeref = [4,9,95]
def toFindbig3(dataArray):
    largestThree = [None,None,None]
    for i in range(1, len(dataArray)):
        updatemyLargestThree(largestThree,i)
    return largestThree

def updatemyLargestThree(largestThree,i):
    if largestThree[2] == None or largestThree[2] < dataArray[i] or largestThree[2] == dataArray[i]:
        updateLargestnum(largestThree,i)
    elif largestThree[1] == None or largestThree[1] < dataArray[i] or largestThree[1] == dataArray[i]:
        updatesecondLargest(largestThree,i)
    elif largestThree[0] == None or largestThree[0] < dataArray[i] or largestThree[0] == dataArray[i]:
        largestThree[0] = dataArray[i]

def updateLargestnum(largestThree,num):
    if largestThree[2] == None or largestThree[2] == dataArray[num]:
        largestThree[2] = dataArray[num]
    else:
        largestThree[0] = largestThree[1]
        largestThree[1] = largestThree[2]
        largestThree[2] = dataArray[num]

def updatesecondLargest(largestThree,num):
    if largestThree[1] == None or largestThree[0] == dataArray[num]:
        largestThree[1] = dataArray[num]
    else:
        largestThree[0] = largestThree[1]
        largestThree[1] = dataArray[num]

print(toFindbig3(dataArray))

print(range(5))

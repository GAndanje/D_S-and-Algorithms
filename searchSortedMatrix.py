import numpy as np

# myMatrix = np.random.randint([])
# print(myMatrix)
p=np.array(([10,12,14],[19,21,29],[35,45,50],[51,62,80]))
#np.info(np.array)
newArray = np.array([[29,49,4],[93,49,2]])
#help(np.array)
print(p)
columnIndex = len(p[1,:])-1
rowIndex = 0
numTosearch = 50
def searchOrderedarray(p,columnIndex,rowIndex,numTosearch):
    myColumnIndex = columnIndex
    print(myColumnIndex)
    myrowIndex = rowIndex
    while (myColumnIndex < len(p[0]) and myColumnIndex>=0) and (myrowIndex >= 0 and myrowIndex<len(p[0])):
        if p[myrowIndex][myColumnIndex] < numTosearch:
            myrowIndex += 1
        elif p[myrowIndex][myColumnIndex] > numTosearch:
            myColumnIndex -= 1
        elif p[myrowIndex][myColumnIndex] == numTosearch:
            return [myrowIndex,myColumnIndex]
    return [-1,-1]

print(searchOrderedarray(p,columnIndex,rowIndex,numTosearch))

def kmp(pattern2Search,string2Search):
    j=i=0
    table=buildTable(pattern2Search)
    while i < len(string2Search):
        if pattern2Search[j]==string2Search[i]:
            if j == len(pattern2Search)-1:
                return True
            j+=1
            i+=1
        elif j>0:
            j=table[j-1]+1
        else:
            i+=1
    return False


def buildTable(stringOject):
    j=1
    i=0
    indexList=len(stringOject)*[-1]
    while i < len(stringOject):
        if j==len(stringOject):
            return indexList
        if stringOject[j]==stringOject[i]:
            indexList[j]=i
            j+=1
            i+=1
        elif i==0:
            j+=1
        elif indexList[i-1]==-1:
            indexList[j]=-1
            i=0
        elif indexList[i-1]>-1:
            i=indexList[i-1]+1
    return indexList

print(kmp("aefaedaefaefa","aefaefaefaedaefaedaefaefa"))

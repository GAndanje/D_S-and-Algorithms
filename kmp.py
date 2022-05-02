def kmp(pattern2Search,string2Search):
    j=i=0
    table=buildTable(pattern2Search)
    while len(string2Search)-i+1>=len(pattern2Search)-j+1:
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
    j=0
    i=1
    indexList=len(stringOject)*[-1]
    while i < len(stringOject):
        if stringOject[j]==stringOject[i]:
            indexList[i]=j
            j+=1
            i+=1
        elif j>0:
            j=indexList[j-1]+1
        else:
            i+=1
    return indexList

print(kmp("aefaedaefaefa1","aefaefaefaedaefaedaefaefa"))

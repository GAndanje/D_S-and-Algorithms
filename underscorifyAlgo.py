def underscorifyAlgorithm(stringtoscorify,stringtosearch):
    locations=collapse(findlocations(stringtoscorify,stringtosearch))
    return underscorify(locations,stringtoscorify)

def findlocations(stringtoscorify,stringtosearch):
    i=0
    locationsList=[]
    while i<len(stringtoscorify):
        found=stringtoscorify.find(stringtosearch,i)
        if found==-1:
            return locationsList
        else:
            locationsList.append([found,found+len(stringtosearch)])
            i=found+1
    return locationsList
print(findlocations("test this is totesttest that testestest is test here","test"))

def collapse(locationsList):
    i=0
    while i<len(locationsList)-1:
        if locationsList[i+1][0]<=locationsList[i][1]:
            locationsList[i][1]=locationsList[i+1][1]
            locationsList.pop(i+1)
        else:
            i+=1
    return locationsList

def underscorify(locations,stringtoscorify):
    underscorifiedString=[]
    underscoreLocations=stripLocations(locations)
    i=j=0
    while i<len(stringtoscorify) and j<len(underscoreLocations):
        if i==underscoreLocations[j]:
            underscorifiedString.append("_")
            underscorifiedString.append(stringtoscorify[i])
            i+=1
            j+=1
        else:
            underscorifiedString.append(stringtoscorify[i])
            i+=1
    while i<len(stringtoscorify):
        underscorifiedString.append(stringtoscorify[i])
        i+=1
    return "".join(underscorifiedString)

def stripLocations(locations):
    strippedLocations=[]
    for i in locations:
        [strippedLocations.append(j) for j in i]
    return strippedLocations

print(underscorifyAlgorithm("try thes system for syssysys is sys sylly sysylly for the sys dev","sys"))



def knapsackProblem(items,capacity):
    myKnapsackvalues =[[0 for x in range(capacity+1)]for y in range(len(items)+1)]
    for rows in range(1,len(items)+1):
        for columns in range(capacity+1):
            if items[rows-1][1]> columns:
                myKnapsackvalues[rows][columns] = myKnapsackvalues[rows-1][columns]
            else:
                myKnapsackvalues[rows][columns] =maximum(rows,columns,items,myKnapsackvalues)
        #print(myKnapsackvalues)
    highvalueitems =[]
    done = False
    maximumcolumn,maximumrow =capacity,len(items)
    print(myKnapsackvalues)
    while not done:
        if maximumrow ==  0:#myKnapsackvalues[maximumrow][maximumcolumn]==0:
            done=True
        elif myKnapsackvalues[maximumrow][maximumcolumn] == myKnapsackvalues[maximumrow-1][maximumcolumn]:
            maximumrow -=1
        elif myKnapsackvalues[maximumrow][maximumcolumn] != myKnapsackvalues[maximumrow-1][maximumcolumn]:
            highvalueitems.append(items[maximumrow-1])
            maximumcolumn -= items[maximumrow-1][1]
            maximumrow -=1
    return myKnapsackvalues,[highvalueitems]

def maximum(rows,columns,items,myKnapsackvalues):
    maximumvalue = max(myKnapsackvalues[rows-1][columns],myKnapsackvalues[rows-1][columns-items[rows-1][1]]+items[rows-1][0]) #[rows-1-(items[rows][1])+items[rows][0]])
    return maximumvalue

print(knapsackProblem([[4,3],[1,2],[5,1],[3,7],[6,5]],10))

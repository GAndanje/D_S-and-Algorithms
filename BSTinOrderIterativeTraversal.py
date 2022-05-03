
class BST:
    def __init__(self,value):
        self.value = value
        self.leftChild=None
        self.rightChild=None
    def insert(self,value):
        currentNode=self
        while True:
            if value<currentNode.value:
                if currentNode.leftChild==None:
                    currentNode.leftChild=BST(value)
                    break
                else:
                    currentNode=currentNode.leftChild
            else:
                if currentNode.rightChild==None:
                    currentNode.rightChild=BST(value)
                    break
                else:
                    currentNode=currentNode.rightChild
        return self
    def search(self,value):
        currentNode=self
        while currentNode!=None:
            if value<currentNode.value:
                currentNode=currentNode.leftChild
            elif value>currentNode.value:
                currentNode=currentNode.rightChild
            else:
                return True
        return False
    def remove(self,value,parentNode=None):
        currentNode=self
        while currentNode is not None:
            if value<currentNode.value:
                parentNode=currentNode
                currentNode=currentNode.leftChild
            elif value>currentNode.value:
                parentNode=currentNode
                currentNode=currentNode.rightChild
            else:
                if currentNode.leftChild is not None and currentNode.rightChild is not None:
                    currentNode.value=currentNode.rightChild.getMinValue()
                    currentNode.rightChild.removeMinValue()
                elif parentNode is None:
                    if currentNode.leftChild is None:
                        currentNode.value=currentNode.rightChild.value
                        currentNode.leftChild=currentNode.rightChild.leftChild
                        currentNode.rightChild=currentNode.rightChild.rightChild
                    else:
                        currentNode.value=currentNode.leftChild.value
                        currentNode.rightChild=currentNode.leftChild.rightChild
                        currentNode.leftChild=currentNode.leftChild.leftChild
                elif parentNode.leftChild == currentNode:
                    parentNode.leftChild=currentNode.leftChild if currentNode.leftChild is not None else currentNode.rightChild
                elif parentNode.rightChild==currentNode:
                    parentNode.rightChild=currentNode.leftChild if currentNode.leftChild is not None else currentNode.rightChild
                break
        return self

    def getMinValue(self):
        currentNode=self
        while currentNode.leftChild is not None:
            currentNode=currentNode.leftChild
        return currentNode.value
    def removeMinValue(self):
        currentNode=self
        while currentNode.leftChild is not None:
            currentNode=currentNode.leftChild
        currentNode=None




myLadder=BST(8)
myLadder.insert(0).insert(2).insert(10).insert(9)
print(myLadder.search(9))
print(myLadder.remove(9))
print(myLadder.search(9))

#inorderTraversal
def inOrderTraversal(BST,callbackfunction):
    previousNode=None
    currentNode=BST
    while currentNode is not None:
        if previousNode ==None or previousNode ==currentNode.parentNode:
            if currentNode.leftChild is not None:
                nextNode=currentNode.leftChild
            else:
                callbackfunction(currentNode)
                nextNode=currentNode.rightChild if currentNode.rightChild is not None else currentNode.parentNode
        elif previousNode==currentNode.leftChild:
            callbackfunction(currentNode)
            nextNode=currentNode.rightChild if rightChild is not None else currentNode.parentNode
        else:
            nextNode=currentNode.parentNode
        previousNode=currentNode
        currentNode=nextNode

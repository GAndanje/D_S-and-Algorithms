class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.prevNode = None
class Dll:
    def __init__(self):
        self.head = None
    def append2Dll(self,data):
        if self.head == None:
            self.head = Node(data)
            return self
        currentNode = self.head
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        currentNode.nextNode =  Node(data)
        currentNode.nextNode.prevNode = currentNode
        return self
    def insert2Dll(self,data,index):
        prevNodepointer = nextNodepointer = indextracker = 0
        if self.head == None:
            self.head = Node(data)
            return self
        currentNode = self.head
        nextNode = currentNode.nextNode
        while indextracker != index:
            if currentNode.nextNode:
                currentNode = currentNode.nextNode
            if currentNode.nextNode:
                nextNode = currentNode.nextNode
            indextracker += 1
            if currentNode ==None:
                break
        if indextracker < index:
            currentNode.nextNode = Node(data)
            currentNode.nextNode.prevNode = currentNode
            print("index out of range.Node defaulted to tail!")
            return self
        else:
            nextNodepointer,prevNodepointer = currentNode.nextNode,currentNode
            _insertHelper(nextNodepointer,prevNodepointer,data)
        return self

    def displayDll(self):
        currentNode = self.head
        Dlllist= []
        while currentNode != None:
            Dlllist.append(currentNode.data)
            currentNode = currentNode.nextNode
        Dlllist.append(None)
        return Dlllist
def _insertHelper(nextNodepointer,prevNodepointer,data):
    currentNode=Node(data)
    prevNodepointer.nextNode = currentNode
    nextNodepointer.prevNode = currentNode
    currentNode.nextNode = nextNodepointer
    currentNode.prevNode = prevNodepointer
def deleteFroDll(self,data):
    pass
    return self
DllObject = Dll()
DllObject.append2Dll(2)
DllObject.append2Dll(3)
DllObject.append2Dll(5)
DllObject.insert2Dll(4,1)
DllObject.append2Dll(5)
DllObject.insert2Dll(1,3)
print(DllObject.displayDll())
print(DllObject.head.nextNode.nextNode.prevNode.prevNode.prevNode)
print(DllObject.head.nextNode.nextNode.nextNode.nextNode.nextNode.prevNode.prevNode.prevNode.prevNode.prevNode.prevNode)

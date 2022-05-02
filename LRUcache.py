class lruCache:
    def __init__(self,maxSize):
        self.hashTable={}
        self.maxSize=maxSize
        self.currentSize=0
        self.DLL=DoublyLL()
    def addToCache(self,key,value):
        if key in self.hashTable:
            if key==self.DLL.head.key:
                self.hashTable[key].data=value
            elif key==self.DLL.head.nextNode.key:
                self.hashTable[key].data=value
                nodeAfterincomingHead=self.hashTable[key].nextNode
                prevHeadNode=self.DLL.head
                self.DLL.head=self.hashTable[key]
                self.DLL.head.prevNode=None
                self.DLL.head.nextNode=prevHeadNode
                prevHeadNode.nextNode=nodeAfterincomingHead
                nodeAfterincomingHead.prevNode=prevHeadNode
                prevHeadNode.prevNode=self.DLL.head

            elif key==self.DLL.getTail().key:
                self.hashTable[key].data=value
                prevHeadNode=self.DLL.head
                nodeB4Tail=self.DLL.getTail().prevNode
                self.DLL.head=self.DLL.getTail()
                self.DLL.head.prevNode=None
                self.DLL.head.nextNode=prevHeadNode
                prevHeadNode.prevNode=self.DLL.head
                nodeB4Tail.nextNode=None
            else:
                self.hashTable[key].data=value
                nodeB4incomingHead=self.hashTable[key].prevNode
                nodeAfterincomingHead=self.hashTable[key].nextNode
                nodeB4incomingHead.nextNode=nodeAfterincomingHead
                nodeAfterincomingHead.prevNode=nodeB4incomingHead
                prevHeadNode=self.DLL.head
                self.DLL.head=self.hashTable[key]
                self.DLL.head.prevNode=None
                self.DLL.head.nextNode=prevHeadNode
                prevHeadNode.prevNode=self.DLL.head
            return self.DLL
        if self.currentSize==0:
            self.hashTable[key]=Node(key,value)
            if self.DLL.head==None:
                self.currentSize+=1
                return self.DLL.addNode(self.hashTable[key])
        if self.currentSize!=self.maxSize:
            self._addKey(key,value)
        else:
            self._updateHshTable(key,value)
        return self.DLL
    def _updateHshTable(self,key,value):
        self._addKey(key,value)
        self._deleteLRU()
    def _addKey(self,key,value):
        newNode=Node(key,value)
        self.hashTable[key]=newNode
        prevHeadNode=self.DLL.head
        self.DLL.head.prevNode=newNode
        self.DLL.head=newNode
        self.DLL.head.nextNode=prevHeadNode
        self.currentSize+=1
    def _deleteLRU(self):
        lru=self.DLL.getTail().key
        newTail=self.DLL.getTail().prevNode
        newTail.nextNode=None
        self.DLL.tail=newTail
        del self.hashTable[lru]
        self.currentSize-=1
    def getMostRecent(self):
        return self.DLL.getTail().key
    def findKey(self,key):
        try:
            return self.hashTable[key].data
        except KeyError:
            return 'KeyError'

class DoublyLL:
    def __init__(self,head=None):
        self.head=head
        self.tail=None
    def addNode(self,Node):
        if self.head==None:
            self.head=Node
            self.tail=Node
            return self
        # currentNode=self.head
        # while currentNode.nextNode!=None:
        #     currentNode=currentNode.nextNode
        # currentNode.nextNode=Node
        # self.tail=Node
    def __str__(self):
        if self.head==None:
            return []
        emptyString=""
        currentNode=self.head
        while currentNode!=None:
            emptyString+=str(currentNode.data)+"->"
            currentNode=currentNode.nextNode
        emptyString+="None"
        return emptyString
    def getHead(self):
        return self.head
    def getTail(self):
        return self.tail

class Node:
    def __init__(self,key,data):
        self.data=data
        self.key=key
        self.prevNode=None
        self.nextNode=None


myCache=lruCache(5)

# myCache.addToCache('chicken',45)
# myCache.addToCache('cows',20)
# print(myCache.addToCache('dogs',4))
# print(myCache.addToCache('cats',2))
# print(myCache.addToCache('sheep',10))
# print(myCache.addToCache('mangoes',1000))
# print(myCache.addToCache('mangoes',.8))
# print(myCache.findKey('jdjljf'))




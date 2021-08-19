class BinaryNode:
    def __init__(self,nodevalue):
        self.nodeValue = nodevalue
        self.leftNode = None
        self.rightNode = None
class BinaryTree:
    def __init__(self,root=None):
        self.root = root
    def add2Tree(self,nodeobject):
        if self.root == None:
            self.root = BinaryNode(nodeobject)
            return self
        currentBNode= self.root
        while True:
            if nodeobject >= currentBNode.nodeValue:
                if currentBNode.rightNode is None:
                    currentBNode.rightNode = BinaryNode(nodeobject)
                    return self
                else:
                    currentBNode = currentBNode.rightNode
            elif nodeobject < currentBNode.nodeValue:
                if currentBNode.leftNode == None:
                    currentBNode.leftNode = BinaryNode(nodeobject)
                    return self
                else:
                    currentBNode = currentBNode.leftNode
BT1 = BinaryTree()       # 100 root                                  100         root
BT1.add2Tree(100)      #  /     \                                    /    \
BT1.add2Tree(150)      # 8     150  rightNode                      8      200        root.rightNode
BT1.add2Tree(200)   #   /     /    \                              /          \
BT1.add2Tree(8)     # None 120        200 rightNode                None         None        root.rightNode.rightnode
                         # /          \
                    #  None             None

BT1.add2Tree(120)
BT1.add2Tree(8)

print(BT1.root.rightNode.)


